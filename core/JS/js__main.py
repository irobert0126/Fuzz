import sys, os


#-----------------------------------------------------------------------#
# The Abstract Factory:
class JSFactory:
    def make_js_cmd(self):   pass
    def make_js_range(self): pass
    def make_html_api(self): pass
    def make_doc_api(self):  pass
    def make_frm_api(self):  pass
    def make_js_obj(self):   pass
    def make_js_init(self):  pass
    
# Anyone who wants to access DOM APIs
# should ONLY use this file. 
# Other details should not be exposed.
class JSEnvironment():
  def __init__(self, factory):
    self.factory = factory
    
  def get_js_api_gen(self):
    return self.factory.make_js_api_gen()
  def get_js_prop_gen(self):
    return self.factory.make_js_prop_gen()
  def get_js_type(self):
    return self.factory.make_js_type()
    
  def get_js_cmd(self):
    return self.factory.make_js_cmd()    
  def get_js_range(self):
    return self.factory.make_js_range()
    
  def get_html_api(self):
    return self.factory.make_html_api()    
  def get_doc_api(self):
    return self.factory.make_doc_api()
    
  def get_js_init(self):
    return self.factory.make_js_init()
    
  def get_js_fuzz_tags(self):
    return self.factory.make_js_fuzz_tags()
  def get_js_fuzz_api(self):
    return self.factory.make_js_fuzz_api()
    
# How Consumer access js APIs.
def factory_unit_test(environment):
  environment.get_js_cmd().unit_test()
  js_range = environment.get_js_range().unit_test()
  environment.get_html_api().unit_test()
  environment.get_doc_api().unit_test()
  js_obj = environment.get_js_obj().unit_test()
  print js_obj.dom_init.init_var_obj
  environment.get_js_init().unit_test(js_range, js_obj)
  
if __name__ == "__main__":
  sys.path.append(os.path.join(os.getcwd(), "core", "JS", "WebKit"))
  webkit_main = importlib.import_module("webkit_main")
  my_env = JSEnvironment(webkit_main.JS_WebKit())
  factory_unit_test(my_env)
