import random

class JS_WIN_API():
  caller = {
    "$$[JS_OBJ??type==DOM_Win&&LorR==r]":1,
  }
  properties = {
  	  # TODO: http://www.html5rocks.com/zh/tutorials/appcache/beginner/
      "applicationCache"		:{
      	"api"		: None,
      	"rtn_type"	: "applicationCache",
      	"rtn"		: "$$[JS_OBJ??type==applicationCache&&LorR==l]",
      },
      "caches"		:{
      	"api"		: None,
      	"rtn_type"	: "CacheStorage",
      	"rtn"		: "$$[JS_OBJ??type==CacheStorage&&LorR==l]",
      	"compatibility": {
      	  "Firefox"		: "1",
      	  "Chrome"		: "0",
      	}
      },
      "closed"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"weight"	: 1
      },
      # TODO: https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto
      "crypto"		:{
      	"api"		: None,
      	"rtn_type"	: "Crypto",
      	"rtn"		: "$$[JS_OBJ??type==Crypto&&LorR==l]",
      	"weight"	: 1
      },
      "defaultStatus"		:{
      	"api"		: None,
      	"rtn_type"	: "str_WindowBar",
      	"rtn"		: "",
      },
      "devicePixelRatio"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      },
      "document"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Doc",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Doc&&LorR==l]",
      },
      "frameElement"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      },
      "frames"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win_List&&LorR==l]",
      },
      "fullScreen"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      },
      # TODO:
      "history"		:{
      	"api"		: None,
      	"rtn_type"	: "History",
      	"rtn"		: "$$[JS_OBJ??type==History&&LorR==l]",
      },
      # TODO: https://developer.mozilla.org/en-US/docs/Web/API/IDBEnvironment/indexedDB
      "indexedDB"		:{
      	"api"		: None,
      	"rtn_type"	: "IDBFactory",
      	"rtn"		: "$$[JS_OBJ??type==IDBFactory&&LorR==l]",
      },
      "innerHeight"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      "innerWidth"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      "length"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      # TODO: https://developer.mozilla.org/en-US/docs/Web/API/Storage
      "localStorage"		:{
      	"api"		: None,
      	"rtn_type"	: "Storage",
      	"rtn"		: "$$[JS_OBJ??type==Storage&&LorR==l]",
      },
      # TODO: https://developer.mozilla.org/en-US/docs/Web/API/Location
      "location"		:{
      	"api"		: None,
      	"rtn_type"	: "Location",
      	"rtn"		: "$$[JS_OBJ??type==Location&&LorR==l]",
      },
      ####################################################################
      "locationbar"		:{
      	"api"		: None,
      	"rtn_type"	: "BarProp",
      	"rtn"		: "$$[JS_OBJ??type==BarProp&&LorR==l]",
      },
      "menubar"		:{
      	"api"		: None,
      	"rtn_type"	: "BarProp",
      	"rtn"		: "$$[JS_OBJ??type==BarProp&&LorR==l]",
      },
      "toolbar"		:{
      	"api"		: None,
      	"rtn_type"	: "BarProp",
      	"rtn"		: "$$[JS_OBJ??type==BarProp&&LorR==l]",
      },
      "statusbar"		:{
      	"api"		: None,
      	"rtn_type"	: "BarProp",
      	"rtn"		: "$$[JS_OBJ??type==BarProp&&LorR==l]",
      },
      "scrollbars"		:{
      	"api"		: None,
      	"rtn_type"	: "BarProp",
      	"rtn"		: "$$[JS_OBJ??type==BarProp&&LorR==l]",
      },
      ####################################################################
      "name"		:{
      	"api"		: None,
      	"rtn_type"	: "str",
      	"rtn"		: "",
      },
      "navigator"		:{
      	"api"		: None,
      	"rtn_type"	: "Navigator",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      	"read-only"	: "1",
      },
      "window"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      },
      "URL"		:{
      	"api"		: None,
      	"rtn_type"	: "URL",
      	"rtn"		: "$$[JS_OBJ??type==URL&&LorR==l]",
      },
      "top"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      },
      "status"		:{
      	"api"		: None,
      	"rtn_type"	: "str",
      	"rtn"		: "",
      },
      "sessionStorage"		:{
      	"api"		: None,
      	"rtn_type"	: "Storage",
      	"rtn"		: "$$[JS_OBJ??type==Storage&&LorR==l]",
      },
      "self"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      },
      "scrollY"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      "scrollX"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      "scrollMaxY"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      "scrollMaxX"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      "screenY"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      },
      "screenX"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      },
      # TODO:
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/screen
      "screen"		:{
      	"api"		: None,
      	"rtn_type"	: "screen",
      	"rtn"		: "$$[JS_OBJ??type==screen&&LorR==l]",
      },
      # TODO:
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/personalbar
      "personalbar"		:{
      	"api"		: None,
      	"rtn_type"	: "personalbar",
      	"rtn"		: "$$[JS_OBJ??type==personalbar&&LorR==l]",
      },
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/performance
      "performance"		:{
      	"api"		: None,
      	"rtn_type"	: "Performance",
      	"rtn"		: "$$[JS_OBJ??type==Performance&&LorR==l]",
      	"compatibility": {
      	  "Chrome"	: "0",
      	}
      },
      "parent"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      },
      "outerWidth"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      	"read-only" : "1",
      },
      "outerHeight"		:{
      	"api"		: None,
      	"rtn_type"	: "int",
      	"rtn"		: "",
      	"read-only" : "1",
      },
      "opener"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      },
      ###############################################################
      "onuserproximity"		:{
      	"api"		: None,
      	"rtn_type"	: "eventHandler",
      	"rtn"		: "$$[JS_OBJ??type==eventHandler&&LorR==l]",
      	"compatibility": { "Firefox" : "0", "Chrome": "0" }
      },
      "ondeviceproximity"		:{
      	"api"		: None,
      	"rtn_type"	: "eventHandler",
      	"rtn"		: "$$[JS_OBJ??type==eventHandler&&LorR==l]",
      	"compatibility": { "Firefox" : "0", "Chrome": "0" }
      },
      "ondeviceorientation"		:{
      	"api"		: None,
      	"rtn_type"	: "eventHandler",
      	"rtn"		: "$$[JS_OBJ??type==eventHandler&&LorR==l]",
      	"compatibility": { "Firefox" : "0", "Chrome": "0" }
      },
      "ondevicemotion"		:{
      	"api"		: None,
      	"rtn_type"	: "eventHandler",
      	"rtn"		: "$$[JS_OBJ??type==eventHandler&&LorR==l]",
      	"compatibility": { "Firefox" : "0", "Chrome": "0" }
      },
      "ondevicelight"		:{
      	"api"		: None,
      	"rtn_type"	: "eventHandler",
      	"rtn"		: "$$[JS_OBJ??type==eventHandler&&LorR==l]",
      	"compatibility": { "Firefox" : "0", "Chrome": "0" }
      },
  }
  api = {
      "$$[JS_OBJ??type==DOM_Win_List&&LorR==r].random"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      	"arg"		: [[ {"$$[int]":1} ]]
      },
      #################################################################
      "atob"		:{
      	"api"		: None,
      	"rtn_type"	: "String",
      	"rtn"		: "$$[JS_OBJ??type==String&&LorR==l]",
      	"arg"		: [[ {"$$[JS_OBJ??type==String_Unicode&&LorR==r]":1} ]]
      },
      "btoa"		:{
      	"api"		: None,
      	"rtn_type"	: "String_Unicode",
      	"rtn"		: "$$[JS_OBJ??type==String_Unicode&&LorR==l]",
      	"arg"		: [[ {"'$$[str]'":1} ]]
      },
      "back"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 100
      },
      "stop"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 10
      },
      "blur"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 100
      },
      "focus"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 100
      },
      "getAttention"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"compatibility": {
      	  "chrome"		: "0",
      	},
      	"weight"	: 100
      },
      "home"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"compatibility": {
      	  "Firefox"		: "1",
      	  "Opera"		: "0",
      	}
      },
      "sizeToContent"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"compatibility": {
      	  "Firefox"		: "1",
      	}
      },
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/open
      "open"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Win",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Win&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[next_frame_url]'":1},
      	    {"'$$[str]'":1},
      	    # "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes"
      	    {"'$$[WindowFeaturesStr]'":0},
      	  ]
      	],
      	"weight"	: 1
      },
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/showModalDialog
      #"showModalDialog"		:{
      #	"api"		: None,
      #	"rtn_type"	: "void",
      #	"rtn"		: "",
      #	"arg"		: [
      #	  [
      #	    {"'$$[next_frame_url]'":1},
      #	    {"'$$[showModalDialog_arguments]'":0},
      #	    {"'$$[showModalDialog_options]'":0},
      #	  ]
      #	]
      #},
      #"close" :{ "api" : None, "rtn_type" : "void", "rtn" : "", "arg" : [[]], "weight"	: 50 },
      #"prompt"		:{
      #	"api"		: None,
      #	"rtn_type"	: "void",
      #	"rtn"		: "",
      #	"arg"		: [[ {"'$$[str]'":1}, {"'$$[str]'":1} ]]
      #},
      #"confirm"		:{
      #	"api"		: None,
      #	"rtn_type"	: "void",
      #	"rtn"		: "",
      #	"arg"		: [[ {"'$$[str]'":1} ]]
      #},
      "dump"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"'$$[str]'":1} ]],
      	"compatibility": {
      	  "Firefox"		: "1",
      	}
      },
      "find"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[str]'":1}, {"$$[bool]":1}, {"$$[bool]":1}, {"$$[bool]":1},
      	    {"$$[bool]":1}, {"$$[bool]":1}, {"$$[bool]":1} ]],
      	"weight"	: 50
      },
      "moveBy"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 2
      },
      "moveTo"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 2
      },
      "resizeBy"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 2
      },
      "resizeTo"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 2
      },
      "scroll"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 50
      },
      "scrollTo"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 50
      },
      "scrollBy"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[float??max==1000]":1}, {"$$[float??max==1000]":1} ]],
      	"weight"	: 50
      },
      "scrollByLines"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[int??max==100&&min==-100]":1} ]],
      	"weight"	: 50
      },
      ############################################################################
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle
      "getComputedStyle"		:{
      	"api"		: None,
      	"rtn_type"	: "CSSStyleDeclaration",
      	"rtn"		: "$$[JS_OBJ??type==CSSStyleDeclaration&&LorR==l]",
      	"arg"		: [
      	  [ {"$$[JS_OBJ??type==DOM_Element&&LorR==r]":1},
      	    {"$$[pseudo-elements]":1},
      	  ]
      	],
      	"weight"	: 50
      },
      "getDefaultComputedStyle"		:{
      	"api"		: None,
      	"rtn_type"	: "CSSStyleDeclaration",
      	"rtn"		: "$$[JS_OBJ??type==CSSStyleDeclaration&&LorR==l]",
      	"arg"		: [
      	  [ {"$$[JS_OBJ??type==DOM_Element&&LorR==r]":1},
      	    {"$$[pseudo-elements]":1},
      	  ]
      	],
      	"weight"	: 50
      },
      "getSelection"		:{
      	"api"		: None,
      	"rtn_type"	: "Selection",
      	"rtn"		: "$$[JS_OBJ??type==Selection&&LorR==l]",
      	"arg"		: [[]],
      	"weight"	: 50
      },
      # TODO: Testing media queries
      # https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Testing_media_queries
      "matchMedia"		:{
      	"api"		: None,
      	"rtn_type"	: "MediaQueryList",
      	"rtn"		: "$$[JS_OBJ??type==MediaQueryList&&LorR==l]",
      	"arg"		: [[ {"'$$[win-mediaQuery-string]'":1} ]],
      	"weight"	: 50
      },
      ############################################################################
      "webkitConvertPointFromNodeToPage"		:{
      	"api"		: None,
      	"rtn_type"	: "WebKitPoint",
      	"rtn"		: "$$[JS_OBJ??type==WebKitPoint&&LorR==l]",
      	"arg"		: [
      	  [ {"$$[JS_OBJ??type==Node&&LorR==r]":1}, 
      	    {"$$[JS_OBJ??type==Point&&LorR==r]":1} ]
      	],
      	"compatibility": {
      	  "Firefox"	:"31",
      	}
      },
      ############################################################################
      "cancelAnimationFrame"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[JS_OBJ??type==Anima_request_id&&LorR==r]":1} ]]
      },
      "requestAnimationFrame"		:{
      	"api"		: None,
      	"rtn_type"	: "Anima_request_id",
      	"rtn"		: "$$[JS_OBJ??type==Anima_request_id&&LorR==l]",
      	"arg"		: [[ {"$$[JS_OBJ??type==Callback&&LorR==r]":1} ]]
      },
      "captureEvents"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[window_capture_events]":1} ]]
      },
      "releaseEvents"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[window_capture_events]":1} ]]
      },
      "setImmediate"		:{
      	"api"		: None,
      	"rtn_type"	: "imediate_id",
      	"rtn"		: "$$[JS_OBJ??type==imediate_id&&LorR==l]",
      	"arg"		: [[ {"$$[JS_OBJ??type==Callback&&LorR==r]":1} ]],
      	"compatibility": {
      	  "IE"		: "10",
      	}
      },
      "clearImmediate"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[JS_OBJ??type==imediate_id&&LorR==r]":1} ]],
      	"compatibility": {
      	  "IE"		: "10",
      	}
      },
      "setInterval"		:{
      	"api"		: None,
      	"rtn_type"	: "interval_id",
      	"rtn"		: "$$[JS_OBJ??type==interval_id&&LorR==l]",
      	"arg"		: [
      	  [ {"$$[JS_OBJ??type==Callback&&LorR==r]":1}, {"$$[float??max==1000]":1} ],
      	  [ {"'$$[rand_js_script]'":1}, {"$$[float??max==1000]":1} ],
      	],
      	"weight"	: 100
      },
      "clearInterval"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[JS_OBJ??type==interval_id&&LorR==r]":1} ]],
      	"weight"	: 80
      },
      "setTimeout"		:{
      	"api"		: None,
      	"rtn_type"	: "timeout_id",
      	"rtn"		: "$$[JS_OBJ??type==timeout_id&&LorR==l]",
      	"arg"		: [
      	  [ {"$$[JS_OBJ??type==Callback&&LorR==r]":1}, {"$$[float??max==1000]":1} ],
      	  [ {"'$$[rand_js_script]'":1}, {"$$[float??max==1000]":1} ]
      	],
      	"weight"	: 100
      },
      "clearTimeout"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ {"$$[JS_OBJ??type==timeout_id&&LorR==r]":1} ]],
      	"weight"	: 80
      },
      ############################################################################
      # https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage
      "postMessage"		:{
      	"api"		: None,
      	"rtn_type"	: "MediaQueryList",
      	"rtn"		: "$$[JS_OBJ??type==MediaQueryList&&LorR==l]",
      	"arg"		: [[ {"'$$[str]'":1}, {"'*'":1} ]],
      	"weight"	: 100
      },
  }
  
  def __init__(self):
    self.window_capture_events = {
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