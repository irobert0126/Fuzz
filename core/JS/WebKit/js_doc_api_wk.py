import random, os, sys
sys.path.append(os.path.join(os.getcwd(),"core"))
import util


class JS_DOC_API():
  caller = {
    "$$[JS_OBJ??type==DOM_Doc&&LorR==r]":1,
  }
  properties = {
    "activeElement": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
    }
  }
  #"close":{ "api" : None, "rtn_type" : "void", "rtn" : "", "arg" : [[]], "weight"	: 100 },
  api = {
      "open"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 100
      },
      "clear"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 100
      },
      "hasFocus"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]],
      	"weight"	: 100
      },
      "webkitCancelFullScreen"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]]
      },
      "webkitExitFullscreen"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]]
      }, 
      "write"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [],
      	  [
      	    {"'$$[Rand_Html]'":1},
      	  ],
      	],
      	"weight"	: 100
      },
      "writeln"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [],
      	  [ {"'$$[Rand_Html]'":1} ],
      	],
      	"weight"	: 100
      },
      "adoptNode"		:{
      	"api"		: None,
      	"rtn_type"	: "Node",
      	"rtn"		: "$$[JS_OBJ??type==Node&&LorR==l]",
      	"arg"		: [
      	  [ {"$$[JS_OBJ??type==Node&&LorR==r]":1} ],
      	],
      	"weight"	: 100
      },
      "importNode"		:{
      	"api"		: None,
      	"rtn_type"	: "Node",
      	"rtn"		: "$$[JS_OBJ??type==Node&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"$$[bool]":1},
      	  ],
      	],
      	"weight"	: 100
      },
      
      ########################################################################
      "createDocumentFragment"		:{
      	"api"		: None,
      	"rtn_type"	: "DocumentFragment",
      	"rtn"		: "$$[JS_OBJ??type==DocumentFragment&&LorR==l]",
      	"arg"		: [[]]
      },
      "createTextNode"		:{
      	"api"		: None,
      	"rtn_type"	: "Node",
      	"rtn"		: "$$[JS_OBJ??type==Node&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[str]'":1},
      	    {"'$$[Rand_Html]'":1},
      	  ]
      	]
      },
      "createComment"		:{
      	"api"		: None,
      	"rtn_type"	: "Node",
      	"rtn"		: "$$[JS_OBJ??type==Node&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[str]'":1},
      	    {"'$$[Rand_Html]'":1},
      	  ]
      	]
      },
      "createProcessingInstruction"		:{
      	"api"		: None,
      	"rtn_type"	: "ProcessingInstruction",
      	"rtn"		: "$$[JS_OBJ??type==ProcessingInstruction&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'xml-stylesheet'":1},
      	    {"'href=\"mycss.css\" type=\"text/css\"'":1},
      	  ]
      	]
      },
      "createAttribute"		:{
      	"api"		: None,
      	"rtn_type"	: "Attr",
      	"rtn"		: "$$[JS_OBJ??type==Attr&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_attr_name]'":1},
      	  ]
      	]
      },
      "createAttributeNS"		:{
      	"api"		: None,
      	"rtn_type"	: "Attr",
      	"rtn"		: "$$[JS_OBJ??type==Attr&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[namespace]'":1},
      	    {"'$$[dom_attr_name]'":1},
      	  ]
      	]
      },
      "createElement"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_tag_name]'":1},
      	  ]
      	]
      },
      "createElementNS"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[namespace]'":1},
      	    {"'$$[dom_tag_name]'":1},
      	  ]
      	]
      },
      "createEvent"		:{
      	"api"		: None,
      	"rtn_type"	: "Event",
      	"rtn"		: "$$[JS_OBJ??type==Event&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_event_type]'":1},
      	  ]
      	],
      	"weight" : 1
      },
      "createRange"		:{
      	"api"		: None,
      	"rtn_type"	: "Range",
      	"rtn"		: "$$[JS_OBJ??type==Range&&LorR==l]",
      	"arg"		: [[]]
      },
      # https://developer.mozilla.org/en-US/docs/Web/API/Document/createNodeIterator
      "createNodeIterator"		:{
      	"api"		: None,
      	"rtn_type"	: "NodeIterator",
      	"rtn"		: "$$[JS_OBJ??type==NodeIterator&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"$$[dom_iter_NodeFilter_whatToShow]":0},
      	    {"$$[dom_iter_NodeFilter_filter]":0},
      	  ],
      	]
      },
      "createTreeWalker"		:{
      	"api"		: None,
      	"rtn_type"	: "TreeWalker",
      	"rtn"		: "$$[JS_OBJ??type==TreeWalker&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"$$[dom_iter_NodeFilter_whatToShow]":1},
      	    {"$$[dom_iter_NodeFilter_filter]":0},
      	    {"$$[bool]":0},
      	  ],
      	]
      },
      "createCDATASection"		:{
      	"api"		: None,
      	"rtn_type"	: "CDATA_Section",
      	"rtn"		: "$$[JS_OBJ??type==CDATA_Section&&LorR==l]",
      	"arg"		: [
      	  [ {"'$$[str]'":1} ],
      	]
      },
      "createExpression"		:{
      	"api"		: None,
      	"rtn_type"	: "XPathExpression",
      	"rtn"		: "$$[JS_OBJ??type==XPathExpression&&LorR==l]",
      	"arg"		: [
      	  [ {"'$$[expression_str]'":1} ,
      	    {"$$[namespaceURLMapper]":1}
      	    #Function namespaceURLMapper (maps a namespace prefix to a namespace URL (or null if none needed))
      	  ],
      	]
      },
      "createNSResolver"		:{
      	"api"		: None,
      	"rtn_type"	: "XPathNSResolver",
      	"rtn"		: "$$[JS_OBJ??type==XPathNSResolver&&LorR==l]",
      	"arg"		: [
      	  [ 
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1}
      	  ],
      	]
      },
      "getSelection"		:{
      	"api"		: None,
      	"rtn_type"	: "Selection",
      	"rtn"		: "$$[JS_OBJ??type==Selection&&LorR==l]",
      	"arg"		: [ [  ] ]
      },
      ##################################################################
      "execCommand"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"$$[DOM_exec_arg]":1} ],
      	],
      	"weight"	: 200
      },
      "queryCommandSupported"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[DOM_exec_name]'":1} ],
      	]
      },
      "queryCommandEnabled"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[DOM_exec_name]'":1} ],
      	]
      },
      "queryCommandState"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[DOM_exec_name]'":1} ],
      	]
      },
      "queryCommandIndeterm"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[DOM_exec_name]'":1} ],
      	]
      },
      "queryCommandValue"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[DOM_exec_name]'":1} ],
      	]
      },
      ##########################################################
      "querySelectorAll"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_selectors]'":1},
      	  ]
      	]
      },
      "querySelector"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_selectors]'":1},
      	  ]
      	]
      },
      "elementFromPoint"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ]
      	],
      	"compatibility": {
      	  "Firefox"	:"31",
      	}
      },
      "elementsFromPoint"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ]
      	],
      	"compatibility": {
      	  "Firefox"	:"31",
      	}
      },
      "getElementById"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_tag_id]'":1},
      	  ]
      	]
      },
      "getElementsByTagName"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_tag_name]'":1},
      	  ]
      	]
      },
      "getElementsByTagNameNS"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[namespace]'":1},
      	    {"'$$[dom_tag_name]'":1},
      	  ]
      	]
      },
      "getElementsByClassName"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_class_name]'":1},
      	  ]
      	]
      },
      "getElementsByName"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_name_name]'":1},
      	  ]
      	]
      },
      #############################################################################
      "evaluate"		:{
      	"api"		: None,
      	"rtn_type"	: "XPathResult",
      	"rtn"		: "$$[JS_OBJ??type==XPathResult&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[JS_OBJ??type==XPathExpression&&LorR==r]":1},
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"$$[JS_OBJ??type==XPathNSResolver&&LorR==r]":1},
      	    {"$$[int??max==9]":1},
      	    {"null":1},
      	  ],
      	  [
      	    {"$$[JS_OBJ??type==XPathExpression&&LorR==r]":1},
      	    {"$$[JS_OBJ??type==Node&&LorR==r]":1},
      	    {"$$[JS_OBJ??type==XPathNSResolver&&LorR==r]":1},
      	    {"$$[int??max==9]":1},
      	    {"$$[JS_OBJ??type==XPathResult&&LorR==r]":1},
      	  ]
      	],
      	"weight"	: 50
      },
      #############################################################################
      "registerElement"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [ {"'$$[str]-$$[str]'":1} ],
      	],
      	"compatibility": {
      	  "Chrome"	:"35",
      	  "Firefox"	:"31",
      	  "Opera"	:"25",
      	  "Android"	:"4.4.4",
      	}
      },
      "exitPointerLock"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [ [ ] ],
      	"compatibility": {
      	  "Chrome"	:"35",
      	  "Firefox"	:"31",
      	}
      },
      # http://html5-demos.appspot.com/static/css/webkit-canvas.html
      # background: -webkit-canvas(mycanvas);
      "getCSSCanvasContext":{
      	"api"		: None,
      	"rtn_type"	: "CanvasRenderingContext2D",
      	"rtn"		: "$$[JS_OBJ??type==CanvasRenderingContext2D&&LorR==l]",
      	"arg"		: [ [
      	  {"'2d'":1},
      	  {"'animation'":1},
      	  {"$$[float??max==1000]":1},
      	  {"$$[float??max==1000]":1},      	  
      	] ],
      	"compatibility": {
      	  "Safari"	:"0",
      	}
      },      
  }
  def __init__(self):
    self.which_doc = {
      "prop": {
        "window.document":[],
        "document":[],
        "contentDocument":["$$[JSRandObj??LorR==rvalue&&type==%s"%(type) for type in ["applet", "frame", "iframe", "object"]],
        "ownerDocument":["$$[JSRandObj??LorR==rvalue&&type==%s"%(type) for type in ["Node", "attribute", "CommentNode", "doctype", "DocumentFragment", "TextNode"]],
      },
      "function": {
        "document.implementation.createDocument": 
          {"args":[{"namespaceURI": "'http://www.w3.org/1999/xhtml'",
                    "qualifiedNameStr": "'html'",
                    "documentType": "null"}],
          },
      }
    } 
    self.XPathResult_Type = {
      "ANY_TYPE":1,
      "NUMBER_TYPE":1,
      "STRING_TYPE":1,
      "BOOLEAN_TYPE":1,
      "UNORDERED_NODE_ITERATOR_TYPE":1,
      "ORDERED_NODE_ITERATOR_TYPE":1,
      "UNORDERED_NODE_SNAPSHOT_TYPE":1,
      "ORDERED_NODE_SNAPSHOT_TYPE":1,
      "ANY_UNORDERED_NODE_TYPE":1,
      "FIRST_ORDERED_NODE_TYPE":1,
    }
    
  def select_XPathResult_Type(self, param={}):
    return util.w_choice(self.XPathResult_Type)
    
  def match_args(self, src_args, targets_args):
     for option in targets_args:
       if option["args"]:
         print ""

  def fill_args(self, fname, argv=None):
   if fname not in self.buildin_func:
     return "%s()" % fname
   if not argv:
     return ",".join([a.values()[0] for a in random.choice(self.buildin_func[fname]["args"])])
     
  def get_template_tag(self):
    return {
      "$$[dom_XPathResultConstants" : {
        "impl" : self.select_XPathResult_Type,
        "help" : "js_doc_api_wk",
        "i.e." : "",
      },
    }
  #############################################################################################
  
  def unit_test(self):
    print "\n[+] JAVASCRIPT DOC API Test:"
    method = "querySelector"
    print "document.%s(%s)" % (method, self.fill_args(method))