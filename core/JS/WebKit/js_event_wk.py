import random, math, os, sys

sys.path.append(os.path.join(os.getcwd(), "core"))
import util

class JS_EVENT():
  dom_event_name = {
    #MouseEvents
    "click":10,"contextmenu":10,"dblclick":10,"mousedown":10,"mouseenter":10,"mouseleave":10,"mousemove":10,
    "mouseover":10,"mouseout":10,"mouseup":10,"scroll":10,"mousewheel":10,
    #Keyboard Events
    "keydown":10,"keypress":10,"keyup":10,
    #Frame/Object Events
    "abort":100,"error":100,"hashchange":100,"load":100,"resize":100,"scroll":100,"unload":100,
    #Form Events
    "blur":10,"change":100,"focus":100, "focusin":100,"focusout":100,
    "input":10,"reset":10,"search":10,"select":10,"submit":10,
    #Drag Events
    "drag":10,"dragend":10,"dragenter":10,"dragleave":10,"dragover":10,"dragstart":10,"drop":10,
    #Clipboard Events
    "copy":10,"cut":10,"paste":10,"beforecopy":10,"beforecut":10,"beforepaste":10,
    #Print Events
    "afterprint":10,"beforeprint":10,
    #Media Events
    "abort":10,"canplay":10,"canplaythrough":10,"durationchange":10,"emptied":10,"ended":10,"error":10,
    "loadeddata":10,"loadedmetadata":10,"loadstart":10,"pause":10,"play":10,"playing":10,"stalled":10,"waiting":10,
    "ratechange":10,"seeked":10,"seeking":10,"suspend":10,"timeupdate":10,"volumechange":10,"progress":10,
    #Animation Events
    # "animationend":10,"animationiteration":10,"animationstart":10,
    #Transition Events
    "transitionend":10,
    #Misc Events
    "online":10,"offline":10,
    "webkitfullscreenchange":10, "webkitfullscreenerror":10,
  }
  # http://help.dottoro.com/ljnxhosf.php
  dom_event_type = {
    #"CompositionEvent" : { "weight":1, "compatibility" : {"IE":1}},
    #"CustomEvent" : { "weight":1, "compatibility" : {"IE":1}},
    #"FocusEvent" : { "weight":1, "compatibility" : {"IE":1}},
    #"KeyEvents" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"DragEvent" : { "weight":1, "compatibility" : {"IE":1, "FireFox":1}},
    #"MouseScrollEvents" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"PopupBlockedEvents" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"PopupEvents" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"MouseWheelEvent" : { "weight":1, "compatibility" : {"IE":1}},
    #"SVGEvent" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"SVGZoomEvent" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"XULCommandEvent" : { "weight":1, "compatibility" : {"FireFox":1}},
    #"XULCommandEvents" : { "weight":1, "compatibility" : {"FireFox":1}},
    "Event" 		: {
      "weight":1,
      "name" : {
        "afterprint":1,
        "beforecopy":1,
        "beforecut":1,
        "beforepaste":1,
        "beforeprint":1,
        "beforeunload":1,
        "blur":1,
        "bounce":1,
        "change":1,
        "CheckboxStateChange":1,
        "copy":1,
        "cut":1,
        "error":1,
        "finish":1,
        "focus":1,
        "hashchange":1,
        "help":1,
        "input":1,
        "load":1,
        "offline":1,
        "online":1,
        "paste":1,
        "RadioStateChange":1,
        "readystatechange":1,
        "reset":1,
        "resize":1,
        "scroll":1,
        "search":1,
        "select":1,
        "selectionchange":1,
        "selectstart":1,
        "start":1,
        "stop":1,
        "submit":1,
        "unload":1,
      }
    },
    "Events" 		: { "weight":1},
    "HTMLEvents" 	: { "weight":1},
    "KeyboardEvent" : { "weight":1},
    "MessageEvent" 	: {
      "weight":1,
      "name" : {
        "message":1,
      }
    },
    "MouseEvent" 	: {
      "weight":1,
      "name" : {
        "click":1,
        "contextmenu":1,
        "dblclick":1,
        "DOMMouseScroll":1,
        "drag":1,
        "dragdrop":1,
        "dragend":1,
        "dragenter":1,
        "dragexit":1,
        "draggesture":1,
        "dragleave":1,
        "dragover":1,
        "dragstart":1,
        "drop":1,
        "mousedown":1,
        "mousemove":1,
        "mouseout":1,
        "mouseover":1,
        "mouseup":1,	
        "mousewheel":1,
      }
    },
    "MouseEvents" 	: { "weight":1},
    "MutationEvent" : {
      "weight":1,
      "name" : {
        "DOMAttrModified":1,
        "DOMCharacterDataModified":1,
        "DOMNodeInserted":1,
        "DOMNodeInsertedIntoDocument":1,
        "DOMNodeRemoved":1,
        "DOMNodeRemovedFromDocument":1,
        "DOMSubtreeModified":1,
      }
    },    	
    "MutationEvents": { "weight":1},
    "OverflowEvent" : {
      "weight":1,
    },
    "ProgressEvent" : { "weight":1},
    "StorageEvent"  : { "weight":1},
    "SVGEvents" 	: { "weight":1},
    "SVGZoomEvents" : { "weight":1},
    "TextEvent" 	: {
      "weight":1,
      "name" : {
        "textInput":1,
      }
    },
    "UIEvent" 		: {
      "weight":1,
      "name" : {
        "abort":1,
        "activate":1,
        "beforeactivate":1,
        "beforedeactivate":1,
        "deactivate":1,
        "DOMActivate":1,
        "DOMFocusIn":1,
        "DOMFocusOut":1,
        "overflow":1,
        "resize":1,
        "scroll":1,
        "select":1,
        "underflow":1,
      }
    },    	
    "UIEvents" 		: { "weight":1},
    "WheelEvent" 	: { "weight":1},
  }
  register_window_event = {
	"Event.ABORT":1,
	"Event.BLUR":1,
	"Event.CLICK":1,
	"Event.CHANGE":1,
	"Event.DBLCLICK":1,
	"Event.DRAGDDROP":1,
	"Event.ERROR":1,
	"Event.FOCUS":1,
	"Event.KEYDOWN":1,
	"Event.KEYPRESS":1,
	"Event.KEYUP":1,
	"Event.LOAD":1,
	"Event.MOUSEDOWN":1,
	"Event.MOUSEMOVE":1,
	"Event.MOUSEOUT":1,
	"Event.MOUSEOVER":1,
	"Event.MOUSEUP":1,
	"Event.MOVE":1,
	"Event.RESET":1,
	"Event.RESIZE":1,
	"Event.SELECT":1,
	"Event.SUBMIT":1,
	"Event.UNLOAD":1
  }
  def __init__(self):
    pass

  def select_dom_event_name(self, param = {}):
    if "type" not in param:
      return util.w_choice(JS_EVENT.dom_event_name)
    else:
      try:
        return util.w_choice(JS_EVENT.dom_event_type[param["type"]]["name"])
      except:
        print "[!] Type (%s) wrong name!" % (param["type"])
        return ""
      
  def select_dom_event_type(self, param = {}):
    return util.w_choice_1(JS_EVENT.dom_event_type)

  def select_1_register_window_event(self, param = {}):
    return util.w_choice(JS_EVENT.register_window_event)
    
  def select_Combo_register_window_event(self, param = {}):
    events = [util.w_choice(JS_EVENT.register_window_event) for i in range(random.randint(1,8))]
    return "|".join(events)

  def get_template_tag(self):
    return {
      "$$[dom_event_name" : {
        "impl" : self.select_dom_event_name,
        "help" : "js_event_wk",
        "i.e." : "",
      },
      "$$[dom_event_type" : {
        "impl" : self.select_dom_event_type,
        "help" : "js_event_wk",
        "i.e." : "",
      },
      "$$[window_capture_events" : {
        "impl" : self.select_Combo_register_window_event,
        "help" : "js_event_wk",
        "i.e." : "",
      }
    }