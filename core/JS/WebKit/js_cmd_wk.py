import random
import js_conf

class JS_CMD():
  def __init__(self, js_cmd_list=None):
    if not js_cmd_list:
      js_cmd_list = js_conf.load_js_cmd()
    self.js_cmd_list = js_cmd_list

  def rand_cmd_name(self, cmd=None):
    return random.choice(self.js_cmd_list.keys())

  def rand_cmd_args(self, key=None):
    if not key:
      key = self.rand_cmd_name()
    return self.js_cmd_list[key]["value"] if key in self.js_cmd_list else ""

  def rand_cmd_full(self, param={}):
    key = param["key"] if "key" in param else None
    if not key:
      key = self.rand_cmd_name()
    args = self.rand_cmd_args(key)
    return "'%s',%s" % (key, args)

  def get_template_tag(self):
    return {
      "$$[DOM_exec_arg" : {
        "impl" : self.rand_cmd_full,
        "help" : "js_cmd_wk",
        "i.e." : "",
      },
      "$$[DOM_exec_name" : {
        "impl" : self.rand_cmd_name,
        "help" : "js_cmd_wk",
        "i.e." : "",
      },
    }
    
  def unit_test(self):
    print "[+] JS COMMAND Test:"
    print self.rand_cmd_full()