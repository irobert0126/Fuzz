import random, sys, os
import fuzz_impl

sys.path.append(os.getcwd()+"/Portal/")
import Counter

class P_Tree_Node:
  def __init__(self, type = "", text = "", depth=0):
    self.children = []
    self.type = type
    self.text = text
    self.depth = depth
    
  def serialize(self):
    if self.type == "text":
      return self.text
    elif self.type == "tag":
      return self.text
    else:
      return "".join([c.serialize() for c in self.children])

class Parser:
  def __init__(self, port, debug=False, config={"max_recur_depth":70}):
    self.debug = debug
    self.config = config
    self.fuzz_impl = fuzz_impl.Fuzz_Impl(debug)
    self.max_template_depth = 38
    self.loaded_temp = {}
    # URL Specific
    self.parsed_uri = None
    self.iframe_helper = None
    self.root = P_Tree_Node()
        
    self.fuzz_impl.my_fuzz_tags.insert_tag_by_instances({
      "$$[next_main_url" : {
        "impl" : self.next_url_tag,
        "help" : "temp_parser",
        "i.e." : "",
      },
      "$$[next_frame_url" : {
        "impl" : self.next_url_tag,
        "help" : "temp_parser",
        "i.e." : "",
      },
    })
    #self.fuzz_impl.runtime.dump_api_info()
    
  ##############################################################
  def load_templates(self, templates):
    for template in templates:
      with open (template, "r") as myfile:
        self.loaded_temp[template] = self.cur_template=myfile.read()
    
  def use_template(self, temp_path = None):
    self.unparsed_template = self.loaded_temp[temp_path if temp_path else random.choice(self.loaded_temp.keys())]
      
  def select_template(self):
    return self.unparsed_template
  ############## ENTRY POINT ############################
  def parse(self, text, param = {"is_iframe":False}):
    self.root = self.parse_impl(text)
    pre_page = self.root.serialize()
    pre_page = pre_page.replace("@@Navi@@", "3000" if param["is_iframe"] else "6000")
    if "####" in pre_page:
      pre_page = pre_page.replace("####", "$$")
    self.root = self.parse_impl(pre_page)
    return self.root.serialize()
    
  def parse_impl(self, text, depth = 0):
    if depth > self.config.get("max_recur_depth"):
      print "[W] Max Depth Reached"
      return P_Tree_Node("unknown", text, depth)
    my_tokens = self.tokenize(text)
    if len(my_tokens) == 1 and my_tokens[0][0] == "text":
      return P_Tree_Node("text", text, depth)
    cur_node = P_Tree_Node("node", "", depth)
    for token in my_tokens:
      if token[0] == "text":
        cur_node.children.append(P_Tree_Node("text", token[1], depth))
      elif token[0] == "tag":
        unfold = self.unfold_tag(token[1], depth)
        child = self.parse_impl(unfold, depth+1)
        if ("unknown" in child.type):
          cur_node.type = "unknown"
        cur_node.children.append(child)
    return cur_node
        
  def template_to_node(self, text, depth=0):
    node = P_Tree_Node("node", "", 0)
    my_tokens = self.tokenize(text)
    for token in my_tokens:
      node.children.append(P_Tree_Node(token[0], token[1], depth+1))
    return node
    
  def tokenize(self, text):
    tokens = []
    cur_pos = 0
    while(True):
      next_pos = text.find("$$", cur_pos)
      if next_pos == -1:
        tokens.append(["text", text[cur_pos:]])
        return tokens
      tokens.append(["text", text[cur_pos:next_pos]])
      cur_token = [tag for tag in self.fuzz_impl.get_fuzz_tag_names()\
               if text[next_pos:].startswith(tag)]
      if len(cur_token) == 0:
        print "[E] Unknown Tag:", text[cur_pos:cur_pos+20]
        raise
      else:
        end_pos = text.find("]", next_pos)
        tokens.append(["tag", text[next_pos : end_pos+1]])
        cur_pos = end_pos+1

  def process_params(self, str):
    params = {}
    pairs = str.split("&&")
    try:
      for pair in pairs:
        key = pair.split("==")[0]
        value = pair.split("==")[1]
        if "||" in value:
          value = value.split("||")
        params[key] = value
    except:
      print "[%s] Not Valid Tag" % str
      return None
    return params
  
  def unfold_tag(self, tag, depth=0, params=None):
    if "??" in tag:
      params = self.process_params(tag.split("]")[0].split("??")[1])
      tag = tag.split("??")[0] + "]"
    else:
      params = {}
    params["tag"] = tag
    if self.debug:
      print "  Fill Tag  :", tag, params
    #print "[%s]" % tag,
    return self.fuzz_impl.fill_tag(tag[:-1], depth, params)
    
  ##############################################################
  def set_uri(self, parsed_uri):
    self.parsed_uri = parsed_uri
    if not Counter.is_iframe_url(parsed_uri):
      self.iframe_helper = Counter.Frame_Counter()

  def reset(self, parsed_uri=None):
    if self.iframe_helper and not Counter.is_iframe_url(parsed_uri):
      self.iframe_helper.reset(parsed_uri)
    self.fuzz_impl.reset()

  def next_url_tag(self, params={}):
    ###========== URL related TAG============###
    if params["tag"].startswith("$$[next_main_url"):
      return Counter.Counter.Next_Uri(self.parsed_uri)

    if params["tag"].startswith("$$[next_frame_url"):
      new_window_url = self.iframe_helper.add_iframe(self.parsed_uri)
      return new_window_url
      
  def unit_test(self):
    t_str = "$$[gl_web_api??caller==True]"
    t_str = "$$[dom_tree??max_depth==3&&max_width==3&&root==div]"
    t_str = "$$[dom_tree??max_depth==3&&max_width==3]<script>$$[js_web_api??batch==10&&full==1]</script>"
    t_str = [
      "<html>",
      "<body onload='fuzzing()'>",
      "<script>$$[js_helper_statement]</script>",
      "<script>$$[js_init_statement]</script>",
      "<script>$$[gl_web_api??full==1]</script>",
      "<script>function fuzzing(){\n\t$$[js_web_api??try_catch==1&&full==1]\n}</script>",
      "$$[dom_tree??root==div]</body></html>",
    ]
    self.set_uri({'path': '', 'ext': 'html', 'id': 1000, 'fname': 'id_1000-cur_1.html', 'cur': 1})
    self.use_template()
    with open("/Users/tluo/Downloads/tmp.html", "w") as f:
      f.write(self.parse(self.unparsed_template))
  ##############################################################
if __name__ == "__main__":
  #p = Parser(10001, True)
  p = Parser(10001, False)
  p.unit_test()