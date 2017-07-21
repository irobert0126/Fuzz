import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util


class GL_TYPE():
  caller = {
    "":1,
  }
  api = {
      "new ArrayBuffer"		:{
      	"api"		: None,
      	"rtn_type"	: "ArrayBuffer",
      	"rtn"		: "$$[GL_OBJ??type==ArrayBuffer&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Uint8Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Uint8Array",
      	"rtn"		: "$$[GL_OBJ??type==Uint8Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Uint8ClampedArray"		:{
      	"api"		: None,
      	"rtn_type"	: "Uint8ClampedArray",
      	"rtn"		: "$$[GL_OBJ??type==Uint8ClampedArray&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Int8Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Int8Array",
      	"rtn"		: "$$[GL_OBJ??type==Int8Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Int16Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Int16Array",
      	"rtn"		: "$$[GL_OBJ??type==Int16Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Uint16Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Uint16Array",
      	"rtn"		: "$$[GL_OBJ??type==Uint16Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Int32Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Int32Array",
      	"rtn"		: "$$[GL_OBJ??type==Int32Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Uint32Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Uint32Array",
      	"rtn"		: "$$[GL_OBJ??type==Uint32Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Float32Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Float32Array",
      	"rtn"		: "$$[GL_OBJ??type==Float32Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Float64Array"		:{
      	"api"		: None,
      	"rtn_type"	: "Float64Array",
      	"rtn"		: "$$[GL_OBJ??type==Float64Array&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1000]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==TypedArray&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new DataView"		:{
      	"api"		: None,
      	"rtn_type"	: "DataView",
      	"rtn"		: "$$[GL_OBJ??type==DataView&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      # is used to represent a generic, fixed-length raw binary data buffer,
      # similar to the ArrayBuffer object, but in a way that they can be used to 
      # create views on shared memory. Unlike an ArrayBuffer, 
      # a SharedArrayBuffer cannot become detached.
      "new SharedArrayBuffer"		:{
      	"api"		: None,
      	"rtn_type"	: "SharedArrayBuffer",
      	"rtn"		: "$$[GL_OBJ??type==SharedArrayBuffer&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[int??max==6666]":1},
      	  ],
      	]
      },
      # CanvasImageData represents a block of image data
      # that you can use to manipulate canvas images.
      "new ImageData"		:{
      	"api"		: None,
      	"rtn_type"	: "ImageData",
      	"rtn"		: "$$[GL_OBJ??type==ImageData&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[GL_OBJ??type==Uint8ClampedArray&&LorR==r]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[int??max==1000]":1},
      	  ],
      	]
      },
      "new Blob"		:{
      	"api"		: None,
      	"rtn_type"	: "Blob",
      	"rtn"		: "$$[GL_OBJ??type==Blob&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer||ArrayBufferView&&LorR==r]":1},
      	    {"{type : 'text/html'}":1}
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==ArrayBuffer||ArrayBufferView&&LorR==r]":1},
      	    {"{type : 'text/plain'}":1}
      	  ],
      	]
      },
      "new Path2D"		:{
      	"api"		: None,
      	"rtn_type"	: "Path2D",
      	"rtn"		: "$$[GL_OBJ??type==Path2D&&LorR==l]",
      	"arg"		: [
      	  [
      	  ],
      	  [
      	    {"$$[GL_OBJ??type==Path2D&&LorR==r]":1},
      	  ],
      	  [
      	    {"\"M10 10 h 80 v 80 h -80 Z\"":1},
      	  ],
      	]
      },
      ######################################
      "new CanvasRenderingContext2D"		:{
      	"api"		: None,
      	"rtn_type"	: "CanvasRenderingContext2D",
      	"rtn"		: "$$[GL_OBJ??type==CanvasRenderingContext2D&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"g_ctx_gl":1},
      	  ],
      	]
      },
      "new HTMLImageElement"		:{
      	"api"		: None,
      	"rtn_type"	: "HTMLImageElement",
      	"rtn"		: "$$[GL_OBJ??type==HTMLImageElement&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"document.createElement('img')":1},
      	  ],
      	  [
      	    {"document.getElementsByTagName('img').random($$[int??max==10])":1},
      	  ],
      	]
      },
      "new HTMLVideoElement"		:{
      	"api"		: None,
      	"rtn_type"	: "HTMLVideoElement",
      	"rtn"		: "$$[GL_OBJ??type==HTMLVideoElement&&LorR==l]",
      	"arg"		: [
      	  [
      	    {"document.createElement('video')":1},
      	  ],
      	  [
      	    {"document.getElementsByTagName('video').random($$[int??max==10])":1},
      	  ],
      	]
      },
  }
  # A generic type name for a group of types
  group = {
    "TypedArray": {
      "Int8Array":1,
      "Uint8Array":1,
      "Uint8ClampedArray":1,
      "Int16Array":1,
      "Uint16Array":1,
      "Int32Array":1,
      "Uint32Array":1,
      "Float32Array":1,
      "Float64Array":1,
    },
    "ArrayBufferView": {
      "Int8Array":1,
      "Uint8Array":1,
      "Uint8ClampedArray":1,
      "Int16Array":1,
      "Uint16Array":1,
      "Int32Array":1,
      "Uint32Array":1,
      "Float32Array":1,
      "Float64Array":1,
      "DataView":1,
    },
    "CanvasImageSource": {
      "HTMLImageElement":1,
      "HTMLVideoElement":1,
      "HTMLCanvasElement":1,
      "CanvasRenderingContext2D":1,
      #"ImageBitmap":1,
      "ImageData":1,
      "Blob":1,
    }
  }

  def __init__(self):
    self.enable = {
      "BLEND":1,
      "CULL_FACE":1,
      "DEPTH_TEST":1,
      "DITHER":1,
      "POLYGON_OFFSET_FILL":1,
      "SAMPLE_ALPHA_COVERAGE":1,
      "SAMPLE_COVERAGE":1,
      "SCISSOR_TEST":1,
      "STENCIL_TEST":1,
    },
    self.undefined_type = [  
    ]
    
  def get_template_tag(self):
    return {
      "$$[gl_type_enable" : {
        "impl" : self.select_gl_type_enable,
        "help" : "webgl_type",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_type_enable(param={}):
    return util.w_choice(self.gl_type_enable)
    