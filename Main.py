#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

import os, sys, time, datetime, psutil, urlparse, random, shutil
#from Parser import Parser
sys.path.append('core')
from temp_parser import Parser
sys.path.append('Portal')
from Log import Logger
from Report import Reporter
from Counter import Counter
from Counter import CounterPool
from Config import Config
from Print import terminal

# Global Saved Data
myConfig = None
myParsers  = []
myReporter = None
myLogger   = None
myServer   = None
myCounter  = None
mode = "Norm"
myPrint = terminal("Server")
PORT_NUMBER = None
last_main_page = None
max_delay = datetime.timedelta(seconds=100)

# static path
js_lib_path = os.path.join("static", "js")
js_html_path = os.path.join("static", "html")
png_lib_path = os.path.join("static", "img", "png")
crash_smpl_path = os.path.join("static", "crash")

class myHandler(BaseHTTPRequestHandler):
  def return_static_file(self, file_name):
    name, ext = os.path.splitext(file_name)
    if ext == ".js":
      file = open(os.path.join(js_lib_path, file_name))
      return 'application/javascript', file.read()
    if ext == ".png":
      file = open(os.path.join(png_lib_path, file_name))
      return 'image/png', file.read()
    if ext == ".html":
      file = open(os.path.join(js_html_path, file_name))
      return 'text/html', file.read()
    return 'application/javascript', "Cannot Found Static File [%s]" % file_name

  def load_replay_log(self, parsed_uri):
    print "[Replay %s]" % parsed_uri["index"]
    global myLogger
    return myLogger.replay_log(parsed_uri["index"]), 'text/html'
    
  def load_crash_page(self, fname):
    print "[Feeding Crash Sample]", fname
    return open(os.path.join(crash_smpl_path, "5.html")).read(), 'text/html'

  #############################################################

  def crash_le_ba(self, parsed_uri):
    global myLogger, myReporter
    myPrint.error("[Found Crash]")
    parsed_report = myReporter.collect()
    myLogger.save_crash(parsed_uri, parsed_report)
    #return "<h1> Crash Le !? </h1>", 'text/html'
    return self.return_static_file("crashle.html"), 'text/html'
    
  #############################################################
  def heartbeat(self, parsed_uri):
    global last_main_page, max_delay, myCounter
    if not last_main_page:
      return "0"
    if max_delay < (datetime.datetime.now() - last_main_page):
      last_main_page = None
      parsed_uri = myCounter.last_served()
      self.crash_le_ba(parsed_uri)
      return "1"
    return "0"
    
  def update_clock(self, parsed_uri):
    global last_main_page
    if not Counter.is_iframe(parsed_uri):
      last_main_page = datetime.datetime.now()
  #############################################################    
  def serve_page_gen(self, parsed_uri):
    is_iframe = Counter.is_iframe(parsed_uri)
    # Check whether the crash log exist.
    begin = datetime.datetime.now()
    reply_content = self.generate_page_from_tmp(parsed_uri, is_iframe=is_iframe)
    end = datetime.datetime.now()
    print "Delta:", (end - begin)
    if not is_iframe:
      if len(myReporter.is_crash_log_found()) > 0:
        self.crash_le_ba(parsed_uri)
    else:
      if myCounter.check_old_window(parsed_uri) or "max_num_frame_reached" in parsed_uri['fname']:
        return "<html><script>window.close()</script></html>"
    return reply_content

  def generate_page_from_tmp(self, parsed_uri, template=None, is_iframe=False):
    global myPrint, myParser
    myParser.reset(parsed_uri)
    myParser.use_template()
    myParser.set_uri(parsed_uri)
    myPrint.debug("[Begin Generating Page]")
    return myParser.parse(myParser.select_template(), {"is_iframe":is_iframe})
  #############################################################

  def url_signal(self, parsed_uri):
    global myPrint, myCounter 
    myPrint.error(parsed_uri)
    if "heartbeat" in parsed_uri["path"]:
      return self.heartbeat(parsed_uri), 'text/html'
      
    if "found_crash" in parsed_uri["path"]:
      myPrint.error("Report Crash on Port(%s) Url(%s)" % (PORT_NUMBER, parsed_uri["fname"]))
      return self.crash_le_ba(parsed_uri)
    
    if parsed_uri["ext"] != "html":
      return self.return_static_file(parsed_uri["fname"])
            
    if Counter.valid_url(parsed_uri) <> 1:
      myPrint.error("Page-Gen For" % parsed_uri["fname"])
      return "Invalid URL", 'text/html'
    #if myCounter.check_crash(parsed_uri):
    #  myPrint.error("Detect Crash on Port(%s) Url(%s)" % (PORT_NUMBER, parsed_uri["fname"]))
    #  return self.crash_le_ba(parsed_uri)
      
    return None, None

  #Handler for the GET requests
  def do_GET(self):
    global mode, myCounter, myLogger
    reply_content = ""
    sendReply = True
    mode = "Unknown"
    try:
      if "index.html" in self.path:
        self.path = self.path.replace("index.html", "id_1000-cur_9.html")
      if "max_num_frame_reached" in self.path:
        self.do_Send('text/html', "<html><script>window.close()</script></html>")
        return
        
      parsed_uri = Counter.parse_url(self.path)

      reply_content, mimetype = self.url_signal(parsed_uri)
      if not reply_content:
        mode = "Norm"
        mimetype = 'text/html'
        reply_content = self.serve_page_gen(parsed_uri)
        self.update_clock(parsed_uri)

      if sendReply == True:
        self.do_Send(mimetype, reply_content)
    except IOError:
      myPrint.error(sys.exc_info().split("\n")[-1])
      self.send_error(404,'File Not Found: %s' % self.path)
      return None
      
    if mode == "Norm":
      if not Counter.is_iframe(parsed_uri):
        myLogger.clean(parsed_uri)
      myLogger.save(reply_content, parsed_uri)
      myCounter.update_counter(parsed_uri)
          
  def do_Send(self, mimetype, reply_content):
    self.send_response(200)
    self.send_header('Content-type', mimetype)
    self.end_headers()
    self.wfile.write(reply_content)
    
  def do_redirect(self):
    print "##-DO_redirect",
    self.send_response(301)
    self.send_header('Location','http://localhost:%s/%d.html' % (PORT_NUMBER, (myReporter.cur_index+1)%9))
    self.end_headers()

if __name__ == "__main__":
  global Config, myReporter, myLogger, myServer, PORT_NUMBER
  myConfig = Config(sys.argv[1] if (len(sys.argv) > 1) else None)
  PORT_NUMBER = myConfig.get("port")
  global gl_template_list
  #gl_template_list = myConfig.get("template")
  gl_template_list = myConfig.get("debug")
  global myCounter
  myCounter  = CounterPool()
  try:
	myParser   = Parser(PORT_NUMBER, False, myConfig)
	myParser.load_templates(gl_template_list)
	myReporter = Reporter(PORT_NUMBER)
	myLogger   = Logger(PORT_NUMBER)
	myServer = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	myServer.serve_forever()
  except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	myServer.socket.close()
