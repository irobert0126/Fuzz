import random, string

class util:
  api = {}
  def get_template_tag(self):
    return {
      "$$[int" : {
        "impl" : get_rand_int,
        "help" : "util",
        "i.e." : "",
      },
      "$$[float" : {
        "impl" : get_rand_float,
        "help" : "util",
        "i.e." : "",
      },
      "$$[str" : {
        "impl" : get_rand_string,
        "help" : "util",
        "i.e." : "",
      },
      "$$[bool" : {
        "impl" : get_rand_bool,
        "help" : "util",
        "i.e." : "",
      },
      "$$[color" : {
        "impl" : get_rand_color,
        "help" : "util",
        "i.e." : "",
      },
      "$$[RandUrl" : {
        "impl" : get_rand_color,
        "help" : "util",
        "i.e." : "",
      },
    }

def w_choice_1(choices):
   total = sum(w["weight"] for c, w in choices.iteritems())
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices.iteritems():
      if upto + w["weight"] > r:
         return c
      upto += w["weight"]
   print choices
   assert False, "Shouldn't get here"

def w_choice(choices):
   total = sum(w for c, w in choices.iteritems())
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices.iteritems():
      if upto + w > r:
         return c
      upto += w
   assert False, "Shouldn't get here"

def get_rand_string(params=None):
  if not params or "len" not in params:
    return ''.join(random.choice(string.ascii_uppercase) for i in range(5))
  return ''.join(random.choice(string.ascii_uppercase) for i in range(params["len"]))
  
def get_rand_int(params=None):
  return str(random.randint(
    0 if "min" not in params else int(params["min"]),
    100 if "max" not in params else int(params["max"])))

def get_rand_float(params=None):
  return get_rand_int(params) + "." + str(random.randint(0, 1000))

def get_rand_bool(params=None):
  return random.choice(["true", "false"])

def get_rand_color(params=None):
  return random.choice(["blue", "red"])
  
def Js_Helper_Define():
  declaration = [
    #"var cur_uri = window.location.href;",
    #"var next = cur_uri.replace(/\d.html/g, function my(x){return (parseInt(x.split(\".\")[0])+1)%9 + \".\"+ x.split(\".\")[1];});",
    "var next = \"$$[next_url]\";",
    "setTimeout( function(){ window.location.href = next;}, 4000);",
    "document.getElementById('next').href=next;",
    "var ECntr=0; setTimeout(function(){ pp(ECntr);}, 999);",
    "var walker0;",
    "var itrtr0;",
    "Array.prototype.random = function (seed) { return this[Math.floor((seed*this.length))];}",
    "Object.prototype.random = function (seed) { return this[Math.floor((seed*this.length))];}",
    "function pp(info) { console.log(info);}",
    "function getErrorObject(){ try { throw Error('') } catch(err) { return err; } }",
    helper_event, helper_mouse_event, helper_mutation_event, helper_ui_event, helper_text_event
  ]
  return "\n".join(declaration)

helper_mouse_event = "\
function InitMouseEvent(target,name,bubbles,cancelable,SX,XY,CX,CY,cK,aK,sK,mK) {\
  if (document.createEvent) {\
    var mousedownEvent = document.createEvent('MouseEvent');\
    mousedownEvent.initMouseEvent (name,bubbles,cancelable,window,0,SX,XY,CX,CY,cK,aK,sK,mK,0,null);\
    target.dispatchEvent (mousedownEvent);\
  } else {\
    if (document.createEventObject) {\
      var mousedownEvent = document.createEventObject (window.event);\
      mousedownEvent.button = 1;\
      target.fireEvent ('on'+name, mousedownEvent);\
    }\
  }\
}"
helper_event = "\
function InitEvent(target,name,bubbles,cancelable) {\
  if (document.createEvent) {\
    var mousedownEvent = document.createEvent('Event');\
    mousedownEvent.initEvent (name,bubbles,cancelable);\
    target.dispatchEvent (mousedownEvent);\
  } else {}\
}"
#action:MutationEvent.MODIFICATION|ADDITION|REMOVAL
helper_mutation_event = "\
function InitMutationEvent(target,name,bubbles,cancelable,attr,value,action){\
  Event = document.createEvent('MutationEvent');\
  Event.initMutationEvent(name,bubbles,cancelable,target.input.getAttributeNode(attr),null,value,attr,action);\
  target.dispatchEvent(Event);\
}"
#detail:0, 1, 2
helper_ui_event = "\
function InitUIEvent(target,name,bubbles,cancelable,detail){\
  Event = document.createEvent('UIEvent');\
  Event.initMutationEvent(name,bubbles,cancelable,window,detail);\
  target.dispatchEvent(Event);\
}"
helper_text_event = "\
function InitTextEvent(target,name,bubbles,cancelable,data,inputMethod,locale){\
  Event = document.createEvent('TextEvent');\
  Event.initTextEvent(name,bubbles,cancelable,null,data,inputMethod,locale);\
  target.dispatchEvent(Event);\
}"


if __name__ == "__main__":
 tree_walker_filter = {
  "NodeFilter.SHOW_ALL":100,
  "NodeFilter.SHOW_ATTRIBUTE":2,
  "NodeFilter.SHOW_CDATA_SECTION":2,
  "NodeFilter.SHOW_COMMENT":2,
  "NodeFilter.SHOW_DOCUMENT":2,
  "NodeFilter.SHOW_DOCUMENT_FRAGMENT":2,
  "NodeFilter.SHOW_DOCUMENT_TYPE":2,
  "NodeFilter.SHOW_ELEMENT":100,
  "NodeFilter.SHOW_ENTITY":2,
  "NodeFilter.SHOW_ENTITY_REFERENCE":2,
  "NodeFilter.SHOW_NOTATION":2,
  "NodeFilter.SHOW_PROCESSING_INSTRUCTION":2,
  "NodeFilter.SHOW_TEXT":50,
 }
 print w_choice(tree_walker_filter)

 buildin_func = {
      "open"                : {"status":1, "weight":1,       "rtn":"", "args":[], "spec":{}},
      "close"               : {"status":1, "weight":0.1,       "rtn":"", "args":[], "spec":{}},
 }
 print w_choice_1(buildin_func)
