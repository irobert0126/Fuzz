#!/usr/bin/python
import os, sys, sched, time, psutil, subprocess, urllib2, shutil
from threading import Timer

log_folder = os.path.join(os.getcwd(), "Log")

# Global Saved Data

safari_count = 1
sshPath = ""
domain = ""
port = ""
tabs_num = ""

def clean_pool():
  dirty_file = os.path.join("server", "pool", "html", "dirty.log")
  with open(dirty_file, "r") as f:
    for line in f.readlines():
      try:
        print "rm:", line
        shutil.rmtree(line.rstrip())
      except:
        print sys.exc_info()
        pass
  with open(dirty_file, "w") as f:
    f.write("")

def Monitor_Safari():
  global safari_count
  #try:
  #  content = urllib2.urlopen("http://localhost:10001/heartbeat/1.html").read()
  #  print "heartbeat:", content
  #except:
  #  print "///"
  #  content = 1
    
  #clean_pool()
  #if "0" in str(content):
  #  time.sleep(20)
  print "[Restarting ... ]"
  find_process_by_name("SafariForWebKitDevelopment", True)
  find_process_by_name("Safari", True)
  find_process_by_name("com.apple.WebKit.Networking", True)
  Restart_Safari(safari_count)
  Timer(300, Monitor_Safari).start()

def Restart_Safari(num):
  global safari_array
  print "[+] Restart SafariForWebKitDevelopment %s\n\n" % num
  os.system("rm -r ~/Library/Saved\\ Application\\ State/com.apple.Safari.savedState")
  #safari_array = [subprocess.Popen(["open", "-n", "-a", "/Applications/Safari.app/Contents/MacOS/SafariForWebKitDevelopment"]) for i in range(num)]
  #safari = subprocess.Popen(["open", "-n", "-a", "/Applications/Safari.app/Contents/MacOS/SafariForWebKitDevelopment"])
  safari = subprocess.Popen(["open", "-n", "-a", "/Applications/Safari.app/Contents/MacOS/Safari"])
  time.sleep(5)
  subprocess.Popen(["osascript", "./setup/safari_tabs_only.scpt", domain, port, tabs_num])

def find_process_by_name(PROCNAME, kill=False):
  found = 0
  for proc in psutil.process_iter():
    try:
      if PROCNAME == proc.name():
        print "Find Process:", proc.name()
        if kill:
          proc.kill()
    except:
      print "Fail To Kill", PROCNAME
    found += 1
  return found
  

if __name__ == "__main__":
  #report.sshPath = str(sys.argv[1]) if len(sys.argv)>1 else ""
  domain = str(sys.argv[2]) if len(sys.argv)>2 else "localhost"
  port = str(sys.argv[3]) if len(sys.argv)>3 else "10001"
  tabs_num = str(sys.argv[1]) if len(sys.argv)>1 else "1"

  os.environ["DYLD_FORCE_FLAT_NAMESPACE"]="1"
  os.environ["DYLD_INSERT_LIBRARIES"]="/usr/lib/libgmalloc.dylib:/System/Library/Frameworks/OpenGL.framework/Versions/A/Resources/GLEngine.bundle/GLEngine:%s/setup/libObjCDYLIB.dylib"%(os.getcwd())
  print os.environ
  find_process_by_name("SafariForWebKitDevelopment", True)
  find_process_by_name("Safari", True)
  Restart_Safari(tabs_num)
  Monitor_Safari()
