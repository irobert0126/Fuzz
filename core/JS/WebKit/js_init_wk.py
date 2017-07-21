import random, os, sys

sys.path.append(os.path.join(os.getcwd(), "core"))
import util

class JS_INIT():
  helper_statement = [
    "window.focus();",
    "var next = \"$$[next_main_url]\";",
    "setTimeout( function(){ window.location.href = next;}, @@Navi@@);",
    "setTimeout( function(){ window.location.href = next;}, @@Navi@@);",
    "setTimeout( function(){ window.location.href = next;}, @@Navi@@);",
    "var mywrapper = function(func, cond, rtn) {\
      return function() {\
        var args = Array.prototype.slice.call(arguments)[0];\
        console.log(cond(args));\
        if(cond(args)) { return rtn(args); } return func(args);}};",
    "function is_invalid(obj) { return (typeof obj === 'undefined') || (obj === null); }",
    "Array.prototype.random = function (seed) { return this[Math.floor((seed*this.length))];}",
    "Object.prototype.random = function (seed) { return this[Math.floor((seed*this.length))];}",
    "window.open = mywrapper(window.open, function(u){if(u.indexOf('max_num_frame_reached')>=0){return true;}else{return false;}},function(){return window;});",
	"var iTable;",
    "function pp(data) { console.log(data); }",
  ]

  init_statement = [
    "document.body.contentEditable=true;",
    "document.designMode='on';",
    "if(is_invalid(window.opener)) {window.opener = window;}",
    "try{iTable = $$[JS_OBJ??type==DOM_Doc&&LorR==r].getElementsByTagName('table').random;}catch(e){iTable = document.createElement('table');$$[JS_OBJ??type==DOM_Doc&&LorR==r].appendChild(iTable);}",
  ]

  def __init__(self): 
    pass
    
  def get_js_helper_statement(self, params= {}):
    return "\n\t".join(JS_INIT.helper_statement)
  def js_init_statement(self, params= {}):
    return "\n\t".join(JS_INIT.init_statement)
    
  def get_template_tag(self):
    return {
      "$$[js_helper_statement" : {
        "impl" : self.get_js_helper_statement,
        "help" : "js_api_gen",
        "i.e." : "",
      },
      "$$[js_init_statement" : {
        "impl" : self.js_init_statement,
        "help" : "js_api_gen",
        "i.e." : "",
      },
    }
    
  def unit_test(self, js_range, js_obj):
    print "[+] JavaScript INIT Test:"
    
    