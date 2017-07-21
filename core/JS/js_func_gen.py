import random, os, sys
sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class JS_FUNC_GEN():
  def __init__(self):
    pass
    
  def js_func_gen(self, param = {}):
    return "function(){$$[js_web_api??try_catch==1&&batch==%s&&full==1]}" % random.randint(1, 15)

  def get_template_tag(self):
    return {
      "$$[JS_Func" : {
        "impl" : self.js_func_gen,
        "help" : "",
        "i.e." : "",
      }
    }