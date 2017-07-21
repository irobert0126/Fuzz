import random, sys, os
sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class DOM_Element_API:
  caller = {
      "$$[JS_OBJ??type==DOM_Element&&LorR==r]":1,
  }
  properties = {
      "attributes": {
      	"api"		: None,
      	"rtn_type"	: "NamedNodeMap",
      	"rtn"		: "$$[JS_OBJ??type==NamedNodeMap&&LorR==l]",
      	"read_only"	: 1,
      },
      "innerHTML": {
      	"api"		: None,
      	"rtn_type"	: "HTML",
      	"rtn"		: "'$$[RandHtml]'",
      },
      "outerHTML": {
      	"api"		: None,
      	"rtn_type"	: "HTML",
      	"rtn"		: "'$$[Rand_Html]'",
      },      
  }
  api = {
      "getClientRects"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_ClientRect_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_ClientRect_List&&LorR==l]",
      	"arg"		: [[ ]],
      	"weight"	: 100
      },
      # TODO: Range
      "webkitGetRegionFlowRanges"		:{
      	"api"		: None,
      	"rtn_type"	: "??",
      	"rtn"		: "",
      	"arg"		: [[ ]]
      },
      "webkitRequestFullScreen"		:{
      	"api"		: None,
      	"rtn_type"	: "",
      	"rtn"		: "",
      	"arg"		: [[ ]]
      },
      "closest"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"arg"		: [[ 
      	  {"'$$[dom_selectors]'":1}
      	]],
      	"weight"	: 100
      },
      "matches"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [[ 
      	  {"'$$[dom_selectors]'":1}
      	]],
      	"weight"	: 100
      },
      "webkitMatchesSelector"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [[ 
      	  {"'$$[dom_selectors]'":1}
      	]]
      },
      "querySelectorAll"		:{
      	"api"		: None,
      	"rtn_type"	: "Element_List",
      	"rtn"		: "$$[JS_OBJ??type==Element_List&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_selectors]'":1},
      	  ]
      	]
      },
      "querySelector"		:{
      	"api"		: None,
      	"rtn_type"	: "Element",
      	"rtn"		: "$$[JS_OBJ??type==Element&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"'$$[dom_selectors]'":1},
      	  ]
      	]
      },
      "removeAttribute"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"'$$[dom_attr_name]'":1},
      	  ]
      	],
      	"weight"	: 100
      },
      "insertAdjacentHTML"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"'$$[dom_position]'":1},
      	    {"'$$[Rand_Html]'":1},
      	  ]
      	],
      	"weight"	: 100
      },
      ############# EVENT RELATED ##############
      "addEventListener"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"'$$[dom_event_name]'":1},
      	    {"$$[JS_OBJ??type==Callback&&LorR==r]":1},
      	    {"$$[bool]":0},
      	  ]
      	],
      	"weight"	: 200
      },   
      "removeEventListener"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"'$$[dom_event_name]'":1},
      	    {"'$$[str]'":1},
      	  ]
      	],
      	"weight"	: 50
      },   
      "dispatchEvent"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[JS_OBJ??type==Event&&LorR==r]":1},
      	  ]
      	],
      	"weight"	: 150
      },
  }
    
  def __init__(self):
   self.position = {
        'beforebegin':1,
        'afterbegin':1,
        'beforeend':1,
        'afterend':1,
    }  
      
  def get_template_tag(self):
    return {
      "$$[dom_position" : {
        "impl" : self.select_position,
        "help" : "js_node",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_position(self, param={}):
    return util.w_choice(self.position)
    
class DOM_Node_API:
    caller = {
      "$$[JS_OBJ??type==DOM_Node&&LorR==r]":1,
    }
    properties = {
      "baseURI": {
      	"api"		: None,
      	"rtn_type"	: "URL",
      	"rtn"		: "$$[JS_OBJ??type==URL&&LorR==l]",
      	"read_only"	: 1,
      },
      "namespaceURI": {
      	"api"		: None,
      	"rtn_type"	: "URL",
      	"rtn"		: "$$[JS_OBJ??type==URL&&LorR==l]",
      	"read_only"	: 1,
      },
      "childNodes": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Node_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node_List&&LorR==l]",
      	"read_only"	: 1,
      },
      "firstChild": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"read_only"	: 1,
      },
      "lastChild ": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"read_only"	: 1,
      },
      "nextSibling": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"read_only"	: 1,
      },
      "previousSibling": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"read_only"	: 1,
      },
      "parentNode": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"read_only"	: 1,
      },
      "parentElement": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"read_only"	: 1,
      },
      "children": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element_List&&LorR==l]",
      	"read_only"	: 1,
      },
      "firstElementChild": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"read_only"	: 1,
      },
      "lastElementChild ": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"read_only"	: 1,
      },
      "nextElementSibling": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"read_only"	: 1,
      },
      "previousElementSibling": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Element",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Element&&LorR==l]",
      	"read_only"	: 1,
      },
      
      # https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeValue
      "nodeValue": {
      	"api"		: None,
      	"rtn_type"	: "ProcessingInstruction ",
      	"rtn"		: "$$[JS_OBJ??type==ProcessingInstruction&&LorR==l]",
      },
      "textContent": {
      	"api"		: None,
      	"rtn_type"	: "DOMString",
      	"rtn"		: "$$[JS_OBJ??type==DOMString&&LorR==l]",
      },
      "ownerDocument": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Doc",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Doc&&LorR==l]",
      	"read_only"	: 1,
      },
      
      "classList": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Class_List",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Class_List&&LorR==l]",
      	"read_only"	: 1,
      },
      "className": {
      	"api"		: None,
      	"rtn_type"	: "DOM_Class_Name",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Class_Name&&LorR==l]",
      },
      
      # nodeType
      # localName
      # prefix
    }
    api = {
      "normalize"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ ]]
      },
      "hasChildNodes"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ ]]
      },
      "isSameNode"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "isEqualNode"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "contains"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "compareDocumentPosition"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      
      "remove"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [[]]
      },
      "replaceChild"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1},
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "removeChild"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "appendChild"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "insertBefore"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      "cloneNode"		:{
      	"api"		: None,
      	"rtn_type"	: "DOM_Node",
      	"rtn"		: "$$[JS_OBJ??type==DOM_Node&&LorR==l]",
      	"arg"		: [[ 
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1},
      	  {"$$[JS_OBJ??type==DOM_Node&&LorR==r]":1}
      	]]
      },
      
      #"isDefaultNamespace"		:{
      #	"api"		: None,
      #	"rtn_type"	: "bool",
      #	"rtn"		: "",
      #	"arg"		: [[ {"$$[namespaceURI]":1}]]
      #},
      #"lookupNamespaceURI"		:{
      #	"api"		: None,
      #	"rtn_type"	: "Variant",
      #	"rtn"		: "$$[JS_OBJ??type==Variant&&LorR==l]",
      #	"arg"		: [[ {"$$[prefix]":1}]]
      #},
      #"isSupported"		:{
      #	"api"		: None,
      #	"rtn_type"	: "bool",
      #	"rtn"		: "",
      #	"arg"		: [[ {"$$[feature]":1}, {"$$[version]":1}]]
      #},
    }
    def get_template_tag(self):
      return {  }
      