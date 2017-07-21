import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class WebGLRenderingContext:
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      ####### Drawing paths #######
      "scissor" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "viewport" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
  }
  
class CanvasRenderingContext2D:
  caller = {
    "$$[GL_OBJ??type==CanvasRenderingContext2D&&LorR==r]":1,
  }
  prop = {
      ###### Line styles ######
      "lineDashOffset" : { "$$[float??max==1000]":1 },
      "miterLimit" : { "$$[float??max==1000]":1 },
      "lineJoin" : { "round":1, "bevel":1, "miter":1 },
      "lineCap" : { "round":1, "butt":1, "square":1 },
      "lineWidth" : { "$$[float??max==1000]":1 },
      ###### Text styles ######  
      "direction" : { "ltr":1, "rtl":1, "inherit":1 },
      "textBaseline":{"top":1,"hanging":1,"middle":1,"alphabetic":1,"ideographic":1,"bottom":1},
      "textAlign" : { "left":1,"right":1,"center":1,"start":1,"end":1},
      "font" : { "$$[font-str]":1 },
      ###### Fill and stroke styles ######  
      "fillStyle" : { "$$[color]":1,
      				  "$$[GL_OBJ??type==CanvasGradient&&LorR==r]":1,
      				  "$$[GL_OBJ??type==CanvasPattern&&LorR==r]":1,
      				},
      "strokeStyle":{ "$$[color]":1,
      				  "$$[GL_OBJ??type==CanvasGradient&&LorR==r]":1,
      				  "$$[GL_OBJ??type==CanvasPattern&&LorR==r]":1,
      				},
      "font" : { "$$[font-str]":1 },
      ###### ShadowsEDIT ######  
      "shadowBlur" : { "$$[int??max==10]":1 },
      "shadowColor": { "$$[color]":1 },
      "shadowOffsetX":{"$$[int??max==10]":1 },
      "shadowOffsetY":{"$$[int??max==10]":1 },
      
      "currentTransform" : {"$$[GL_OBJ??type==SVGMatrix&&LorR==r]":1},
  }
  api = {
      ####### Drawing paths #######
      "fill" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [],
      	  [
      	    {"\"$$[ctx_fillRule]\"":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	    {"\"$$[ctx_fillRule]\"":1},
      	  ],
      	],
      	"desc": "fills the current or given path with the current fill style\
      	using the non-zero or even-odd winding rule.",
      	"i.e.": "",
      },
      "stroke" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [ ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "drawFocusIfNeeded" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[DOM_OBJ??type==Node&&LorR==r]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	    {"$$[DOM_OBJ??type==Node&&LorR==r]":1},
      	  ],
      	],
      	"desc": "draws a focus ring around the current path or given path,\
      	If a given element is focused.",
      	"i.e.": "",
      },
      "scrollPathIntoView" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [ ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "clip" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [],
      	  [
      	    {"\"$$[ctx_fillRule]\"":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	    {"\"$$[ctx_fillRule]\"":1},
      	  ],
      	],
      	"desc": "turns the path currently being built into the current clipping path.",
      	"i.e.": "",
      },
      "isPointInPath" : {
      	"api": None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"\"$$[ctx_fillRule]\"":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"\"$$[ctx_fillRule]\"":1},
      	  ],
      	],
      	"desc": "reports whether or not the specified point is contained in the current path.",
      	"i.e.": "",
      },
      "isPointInStroke" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      #######     Paths     #######
      "beginPath" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	  ],
      	],
      	"desc": "Resets the current path.",
      	"i.e.": "ctx.beginPath();",
      },
      "closePath" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	  ],
      	],
      	"desc": "",
      	"i.e.": "ctx.closePath();",
      },
      "moveTo" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "moves the starting point of a new sub-path to the (x, y) coordinates.",
      	"i.e.": "",
      },
      "lineTo" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "connects the last point in the sub-path to the x, y coordinates\
      	 with a straight line (but does not actually draw it).",
      	"i.e.": "",
      },
      "bezierCurveTo" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[float??max==100]":1},
      	  ],
      	],
      	"desc": "Adds a point to the current subpath by using the specified control points\
      	 that represent a cubic Bezier curve.",
      	"i.e.": "ctx.bezierCurveTo(200, 200, 200, 0, 300, 100);",
      },
      "quadraticCurveTo" : {
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "Adds a quadratic Bezier curve to the path",
      	"i.e.": "",
      }, 
      "arc"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[bool]":1},
      	  ],
      	],
      	"desc": "Adds points to a path that represents an arc.",
      	"i.e.": "ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);",
      },
      "arcTo"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[bool]":1},
      	  ],
      	],
      	"desc": "Draws an arc of a fixed radius between two tangents that are defined by\
      	 the current point in a path and two additional points.",
      	"i.e.": "ctx.arcTo(200, 100, 200, 120, 20);",
      },
      "ellipse"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[float??max==100]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[bool]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "void ctx.ellipse(x, y, radiusX, radiusY, rotation, startAngle, endAngle, anticlockwise);",
      },
      "rect"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "creates a path for a rectangle at position (x, y) with a size that\
      	 is determined by width and height.",
      	"i.e.": "",
      },    
      ###### CanvasGradient ######   
      "createLinearGradient"		:{
      	"api": None,
      	"rtn_type"	: "CanvasGradient",
      	"rtn"		: "$$[GL_OBJ??type==CanvasGradient&&LorR==l]",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },    
      "createRadialGradient"		:{
      	"api": None,
      	"rtn_type"	: "CanvasGradient",
      	"rtn"		: "$$[GL_OBJ??type==CanvasGradient&&LorR==l]",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      ###### CanvasPattern ######     
      "createPattern"		:{
      	"api": None,
      	"rtn_type"	: "CanvasPattern",
      	"rtn"		: "$$[GL_OBJ??type==CanvasPattern&&LorR==l]",
      	"arg": [
      	  [
      	    {"$$[GL_OBJ??type==CanvasImageSource&&LorR==r]":1},
      	    {"$$[ctx_repetition]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },      
      ###### Line styles ######      
      "getLineDash"		:{
      	"api": None,
      	"rtn_type"	: "Array",
      	"rtn"		: "$$[GL_OBJ??type==Array&&LorR==l]",
      	"arg": [
      	  [
      	  ],
      	],
      	"desc": " gets the current line dash pattern.",
      	"i.e.": "",
      },     
      "setLineDash"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[GL_OBJ??type==Array&&LorR==r]":1},
      	  ],
      	],
      	"desc": "sets the line dash pattern.",
      	"i.e.": "",
      },  
      ###### Drawing textEDIT ######
      "fillText"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[str]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	  [
      	    {"$$[str]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	],
      	"desc": "fills a given text at the given (x, y) position. If the optional fourth\
      	parameter for a maximum width is provided, the text will be scaled to fit that width.",
      	"i.e.": "void ctx.fillText(text, x, y [, maxWidth]);",
      },
      "strokeText"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[str]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	  [
      	    {"$$[str]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	],
      	"desc": "trokes a given text at the given (x, y) position. If the optional fourth\
      	parameter for a maximum width is provided, the text will be scaled to fit that width.",
      	"i.e.": "void ctx.strokeText(text, x, y [, maxWidth]);",
      },
      "measureText"		:{
      	"api": None,
      	"rtn_type"	: "TextMetrics",
      	"rtn"		: "$$[GL_OBJ??type==TextMetrics&&LorR==l]",
      	"arg": [
      	  [
      	    {"$$[str]":1},
      	  ],
      	],
      	"desc": " returns a TextMetrics object that contains information about the \
      	measured text (such as its width for example).",
      	"i.e.": "void ctx.measureText(text);",
      },
      ###### Drawing rectangles ######
      "clearRect"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "Clears the pixels on a CanvasRenderingContext2D object within a given rectangle.",
      	"i.e.": "clearRect",
      },
      "fillRect"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "draws a filled rectangle at (x, y) position whose size is determined \
      	by width and height and whose style is determined by the fillStyle attribute.",
      	"i.e.": "",
      },
      "strokeRect"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "paints a rectangle which has a starting point at (x, y) and \
      	has a w width and an h height onto the canvas, using the current stroke style.",
      	"i.e.": "",
      },
      ###### TransformationsEDIT ######
      "rotate"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==2]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "scale"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==11]":1},
      	    {"$$[float??max==11]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "translate"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==1000]":1},
      	    {"$$[float??max==1000]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "setTransform"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[float??max==11]":1},
      	    {"$$[float??max==11]":1},
      	    {"$$[float??max==11]":1},
      	    {"$$[float??max==11]":1},
      	    {"$$[float??max==11]":1},
      	    {"$$[float??max==11]":1},
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
      "resetTransform"		:{
      	"api": None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	  ],
      	],
      	"desc": "",
      	"i.e.": "",
      },
  }	
  def __init__(self):
    self.ctx_repetition = {
      "repeat":1,
      "repeat-x":1,
      "repeat-y":1,
      "no-repeat":1,
    }
    self.ctx_fillRule = {
      "nonzero":1,
      "evenodd":1,
    }
 
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[ctx_repetition" : {
        "impl" : self.select_ctx_repetition,
        "help" : "js_canvas",
        "i.e." : "",
      },
      "$$[ctx_fillRule" : {
        "impl" : self.select_ctx_fillRule,
        "help" : "js_canvas",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_ctx_repetition(self, param={}):
    return util.w_choice(self.ctx_repetition)
  def select_ctx_fillRule(self, param={}):
    return util.w_choice(self.ctx_fillRule)
    
# https://developer.mozilla.org/en-US/docs/Web/API/TextMetrics
# The TextMetrics interface represents the dimension of a text in the canvas
class TextMetrics:
  pass