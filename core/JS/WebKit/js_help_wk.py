import random, os, sys

sys.path.append(os.path.join(os.getcwd(), "core"))
import util

class JS_HELP:
  caller = {
    "$$[JS_OBJ??type==DOM_Win&&LorR==r]":1,
  }
  api = {  
    "InitEvent" : {
      "source" : [
        "function InitEvent(name,bubbles,cancelable) {",
        "  var Event = document.createEvent('Event');",
        "  Event.initEvent (name,bubbles,cancelable);",
        "  return Event;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"'$$[dom_event_name??type==Event]'":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	  ]
      	],
      "weight" : 10
    },
    "InitMouseEvent" : {
      "source" : [
        "function InitMouseEvent(name,bubbles,cancelable,view,detail,SX,XY,CX,CY,cK,aK,sK,mK) {",
        "  var mousedownEvent = document.createEvent('MouseEvent');",
        "  mousedownEvent.initMouseEvent (name,bubbles,cancelable,view,detail,SX,XY,CX,CY,cK,aK,sK,mK,0,null);",
        "  return mousedownEvent;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"'$$[dom_event_name??type==MouseEvent]'":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"$$[int??max==10]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ]
      	],
      "weight" : 10
    },
    "InitOverflowEvent": {
      "source" : [
        "function InitOverflowEvent(orient, horizontalOverflow, verticalOverflow){",
        "  Event = document.createEvent('OverflowEvent');",
        "  Event.initOverflowEvent(orient, horizontalOverflow, verticalOverflow);"
        "  return Event;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"$$[int??max==2]":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	  ]
      	],
      "weight" : 10
    },
    "InitMutationEvent": {
      "source" : [
        "function InitMutationEvent(eventName,bubbles,cancelable,relatedNode,prevValue,newValue,attrName,attrChange){",
        "  Event = document.createEvent('MutationEvent');",
        "  Event.initMutationEvent(eventName,bubbles,cancelable,relatedNode,prevValue,newValue,attrName,attrChange);"
        "  return Event;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"'$$[dom_event_name??type==MutationEvent]'":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"'$$[Rand_Html]'":1},
      	    {"'$$[Rand_Html]'":1},
      	    {"'$$[dom_attr_name]'":1},
      	    {"$$[int??min==1&&max==3]":1},
      	  ]
      	],
      "weight" : 10
    },
    "InitUIEvent": {
      "source" : [
        "function InitUIEvent(name,bubbles,cancelable,window,detail){",
        "  Event = document.createEvent('UIEvent');",
        "  Event.initUIEvent(name,bubbles,cancelable,window,detail);"
        "  return Event;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"'$$[dom_event_name??type==UIEvent]'":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	    {"$$[JS_OBJ??type==DOM_Win&&LorR==r]":1},
      	    {"$$[int??max==10]":1},
      	  ]
      	],
      "weight" : 10
    },
    "InitTextEvent": { 
      "source" : [
        "function InitTextEvent(name,bubbles,cancelable,view,data,inputMethod,locale){",
        "  Event = document.createEvent('TextEvent');",
        "  Event.initTextEvent(name,bubbles,cancelable,view,data,inputMethod,locale);"
        "  return Event;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"'$$[dom_event_name??type==TextEvent]'":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	    {"$$[JS_OBJ??type==DOM_Win&&LorR==r]":1},
      	    {"'$$[Rand_Html]'":1},
      	    {"$$[int??max==10]":1},
      	    {"'$$[Rand_Html]'":1},
      	  ]
      	],
      "weight" : 10
    },
    "InitMessageEvent": { 
      "source" : [
        "function InitMessageEvent(name, bubbles, cancelable, data, origin, lastEventId, source, ports){",
        "  Event = document.createEvent('MessageEvent');",
        "  Event.initMessageEvent(name, bubbles, cancelable, data, origin, lastEventId, source, ports);"
        "  return Event;",
        "}" ],
      "rtn_type"	: "Event",
      "rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      "arg"		: [
      	  [
      	    {"'$$[dom_event_name??type==MessageEvent]'":1},
      	    {"$$[bool]":1},
      	    {"$$[bool]":1},
      	    {"'$$[Rand_Html]'":1},
      	    {"'$$[Rand_Html]'":1},
      	    {"'$$[Rand_Html]'":1},
      	    {"$$[JS_OBJ??type==DOM_Win&&LorR==r]":1},
      	    {"null":1},
      	  ]
      	],
      "weight" : 10
    },
  }
   
  def __init__(self): 
    pass
    
  def get_js_helper_atomic(self, params= {}):
    return "\n\n".join(["\n\t".join(JS_HELP.api[k]["source"]) for k in JS_HELP.api.keys()])
    
  def get_template_tag(self):
    return {
      "$$[js_helper_atomic" : {
        "impl" : self.get_js_helper_atomic,
        "help" : "js_api_gen",
        "i.e." : "",
      },
    }
    
  def unit_test(self, js_range, js_obj):
    print "[+] JavaScript INIT Test:"
    
    