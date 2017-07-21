import os, sys, random
import js_conf

sys.path.append(os.path.join(os.getcwd(), ".."))
import js__main, js_cmd_wk, js_range_wk, js_html_api_wk, js_doc_api_wk,\
       js_type, js_api_gen, js_prop_gen

#-----------------------------------------------------------------------#
# Concrete factories:
class JS_WebKit(js__main.JSFactory):
  def make_js_fuzz_tags(self):
    return {
      "js_cmd_wk"		: "JS_CMD",
      "js_api_gen"		: "JS_API_GEN",
      "js_func_gen"		: "JS_FUNC_GEN",
      "js_event_wk"		: "JS_EVENT",
      "js_type"			: "JS_TYPE",
      "js_init_wk"  	: "JS_INIT",
      "js_node_api_wk"	: "DOM_Node_API",
      "js_node_api_wk"	: "DOM_Element_API",
      "js_help_wk"		: "JS_HELP",
    }
  def make_js_api_gen(self):
    return js_api_gen.JS_API_GEN()
  def make_js_prop_gen(self):
    return js_prop_gen.JS_PROP_GEN()
  def make_js_type(self):
    return js_type.JS_TYPE()
  def make_js_cmd(self):
    return js_cmd_wk.JS_CMD(js_conf.load_js_cmd())
  def make_js_range(self):
     return js_range_wk.JS_RANGE()
  def make_html_api(self):
     return js_html_api_wk.JS_HTML_API()
  def make_doc_api(self):
     return js_doc_api_wk.JS_DOC_API()
  def make_js_obj(self):
     return js_obj_wk.JS_OBJ(
     	js_html_api_wk.JS_HTML_API(),
     	js_doc_api_wk.JS_DOC_API(),
     	self.make_js_init()
     )     
  def make_js_init(self):
     return js_init_wk.JS_INIT()
#-----------------------------------------------------------------------#