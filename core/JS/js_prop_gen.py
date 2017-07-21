import importlib, random, os, sys
sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class JS_PROP_GEN():
  def __init__(self, moduleNames={}):
    self.prop = {}
    self.prop_weight = {}
    moduleNames={
      "js_doc_api_wk"	: "JS_DOC_API",
      "js_win_api_wk"	: "JS_WIN_API",
    }
    self.load_prop_from_module_name(moduleNames)

  def load_prop_from_module_name(self, moduleNames):
    for m_name, c_name in moduleNames.iteritems():
      module = importlib.import_module(m_name)
      obj = getattr(module, c_name)
      my_prop = obj.properties
      my_prop_caller_id = {}
      for prop in my_prop:
        if "compatibility" in my_prop:
          continue
        prop_key = "%s--%s" % (c_name, prop)
        my_prop_caller_id[prop_key] = my_prop[prop]
        my_prop_caller_id[prop_key]["caller"] = obj.caller
        my_prop_caller_id[prop_key]["prop"] = prop
      self.prop.update(my_prop_caller_id)
    self.weight_prop()
    
  def weight_prop(self):
    for prop in self.prop.keys():
      if prop not in self.prop_weight:
        self.prop_weight[prop] = 1

  def tag_js_prop(self, param = {}):
    prop_key = param["target"] if "target" in param else util.w_choice(self.prop_weight)
    cur_prop_name = self.prop[prop_key]["prop"]
    if "name_only" in param:
      return cur_prop_name
      
    caller = util.w_choice(self.prop[prop_key]["caller"])
    if "caller" in param and param["caller"]:
      if len(caller) > 0:
        return "%s.%s" % (caller, cur_prop_name)
        
    rtn = self.prop[prop_key]["rtn"]
    if "full" in param and param["full"]:
      if len(caller) > 0 and len(rtn) > 0:
        return "%s = %s.%s;" % (rtn, caller, cur_api_name)
      return "%s.%s" % (caller, cur_prop_name)
    return "?????????"    

  def get_template_tag(self):
    return {
      "$$[js_web_prop" : {
        "impl" : self.tag_js_prop,
        "help" : "",
        "i.e." : "",
      }
    }