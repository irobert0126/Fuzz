import importlib, random, os, sys
sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class JS_API_GEN():
  def __init__(self, moduleNames={}):
    self.api = {}
    self.api_weight = {}
    moduleNames={
      "js_doc_api_wk"	: "JS_DOC_API",
      "js_win_api_wk"	: "JS_WIN_API",
      "js_node_api_wk"	: "DOM_Node_API",
      "js_node_api_wk"	: "DOM_Element_API",
      "js_help_wk"		: "JS_HELP",
    }
    self.load_api_from_module_name(moduleNames)

  def load_api_from_module_name(self, moduleNames):
    for m_name, c_name in moduleNames.iteritems():
      module = importlib.import_module(m_name)
      obj = getattr(module, c_name)
      my_api = obj.api
      my_api_caller_id = {}
      for api in my_api:
        if "compatibility" in my_api[api]:
          continue
        api_key = "%s--%s" % (c_name,api)
        my_api_caller_id[api_key] = my_api[api]
        if "caller" not in my_api_caller_id[api_key]:
          my_api_caller_id[api_key]["caller"] = obj.caller
        my_api_caller_id[api_key]["api"] = api
      self.api.update(my_api_caller_id)
    self.weight_api()
    
  def weight_api(self):
    for api in self.api.keys():
      if api not in self.api_weight:
        self.api_weight[api] = 10 if 'weight' not in self.api[api] else int(self.api[api]['weight'])
        
  def tag_js_script_as_str(self, param = {}):
    batch = int(param["batch"]) if "batch" in param else random.randint(0,10)
    scripts = [self.tag_js_api_helper({"full":1}) for i in range(0, batch)]
    # TODO: NESTED CASE
    #return "".join(scripts).replace("'", "\\'").replace("\"", "\\\"")
    return "eval(console.log(\\'[!Random JS Script!]\\'));"
    
  # Make sure to SET "batch=1" when create Dynamic Runtime Obj
  #              SET "target=API_NAME" to create specific one.
  def tag_js_api(self, param = {}):
    batch = int(param["batch"]) if "batch" in param else random.randint(50,100)
    scripts = []
    for i in range(0, batch):
      if "jjjj" in param and random.randint(0, 10) < 2:
        scripts.append("$$[jjjj]")
      else:
        scripts.append(self.tag_js_api_helper(param))
    if "try_catch" in param:
      scripts = [ "try { %s } catch(err) {pp(err);}" % s for s in scripts]
    return "\n\t".join(scripts)
    
  def tag_js_api_helper(self, param = {}):
    api_key = param["target"] if "target" in param else util.w_choice(self.api_weight)
    cur_api_name = self.api[api_key]["api"]
    
    if "name_only" in param:
      return cur_api_name
    #print cur_api_name, param
    cur_api_args = self.fill_args(api_key, param)
    if "args_only" in param:
      return cur_api_args
    
    caller = util.w_choice(self.api[api_key]["caller"])
    if "caller" in param and param["caller"]:
      if len(caller) > 0:
        return "%s.%s(%s)" % (caller, cur_api_name, cur_api_args)
        
    rtn = self.api[api_key]["rtn"]
    if "full" in param and param["full"]:
      if len(caller) > 0 and len(rtn) > 0:
        return "%s = %s.%s(%s);" % (rtn, caller, cur_api_name, cur_api_args)
      return "%s.%s(%s);" % (caller, cur_api_name, cur_api_args)
    return "%s(%s);" % (cur_api_name, cur_api_args)
    
  def unit_test(self):
    for api_name, api_arg in self.api.iteritems():
      print api_name
      arg = random.choice(api_arg["arg"])
      arg_name = [k.keys()[0] for k in arg]
      print "   %s(%s)" % (api_name, ",".join(arg_name))

  def match_args(self, src_args, targets_args):
     for option in targets_args:
       if option["args"]:
         print ""

  def fill_args(self, fname, argv=None):
    arg = random.choice(self.api[fname]["arg"])
    arg_name = [k.keys()[0] for k in arg]
    return ", ".join(arg_name)

  def get_template_tag(self):
    return {
      "$$[js_web_api" : {
        "impl" : self.tag_js_api,
        "help" : "js_api_gen",
        "i.e." : "",
      },
      "$$[rand_js_script" : {
        "impl" : self.tag_js_script_as_str,
        "help" : "js_api_gen",
        "i.e." : "",
      },
    }