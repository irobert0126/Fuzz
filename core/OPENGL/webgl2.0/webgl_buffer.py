import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_BUFFER():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "createBuffer"		:{
      	"api": None,
      	"rtn_type"	: "WebGLBuffer",
      	"rtn"		: "$$[GL_OBJ??type==WebGLBuffer&&LorR==l]",
      	"arg": [[]]
      },
      "deleteBuffer"		:{
      	"api": None,
      	"rtn_type": "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[GL_OBJ??type==WebGLBuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "bindBuffer"		:{
      	"api": None,
      	"rtn_type": "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[gl_bf_target]":1},
      	    {"$$[GL_OBJ??type==WebGLBuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "bufferData"		:{
      	"api": None,
      	"i.e.": "",
      	"rtn_type": "void",
      	"rtn"	  : "",
      	"arg": [
      	  [
      	    {"$$[gl_bf_target]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[gl_bf_usage]":1},
      	  ],
      	  [
      	    {"$$[gl_bf_target]":1},
      	    {"$$[GL_OBJ??type==ArrayBuffer||SharedArrayBuffer||ArrayBufferView&&LorR==r]":1},
      	    {"$$[gl_bf_usage]":1},
      	  ]
      	]
      },
      "bufferSubData"		:{
      	"api": None,
      	"i.e.": "",
      	"rtn_type": "void",
      	"rtn"	  : "",
      	"arg": [
      	  [
      	    {"$$[gl_bf_target]":1},
      	    {"$$[int??max==1000]":1},
      	    {"$$[GL_OBJ??type==ArrayBuffer||SharedArrayBuffer||ArrayBufferView&&LorR==r]":1},
      	  ]
      	]
      },
      "isBuffer"		:{
      	"api": None,
      	"i.e.": "",
      	"rtn_type": "void",
      	"rtn"	  : "",
      	"arg": [
      	  [
      	    {"$$[GL_OBJ??type==WebGLBuffer&&LorR==r]":1}
      	  ]
      	]
      },
  }
  def __init__(self):
    self.gl_bf_target = {
      "ARRAY_BUFFER":1,
      "ELEMENT_ARRAY_BUFFER":1, 
    }
    self.gl_bf_usage = {
	  "STATIC_DRAW"	:1,
	  "STREAM_DRAW"	:1,
	  "DYNAMIC_DRAW":1,
	}
	
  def get_template_tag(self):
    return {
      "$$[gl_bf_target" : {
        "impl" : self.select_gl_bf_target,
        "help" : "webgl_buffer",
        "i.e." : "",
      },
      "$$[gl_bf_usage" : {
        "impl" : self.select_gl_bf_usage,
        "help" : "webgl_buffer",
        "i.e." : "",
      },
    }

  #=================================================================================#
  def select_gl_bf_target(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_bf_target)
  def select_gl_bf_usage(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_bf_usage)

"""
Object createBuffer( void )
	Create a WebGLBuffer buffer object
void deleteBuffer( Object buffer )
	Delete a WebGLBuffer buffer object
void bindBuffer( ulong target, Object buffer )
	Bind a buffer object. Accepted values for target are:
	ARRAY_BUFFER ELEMENT_ARRAY_BUFFER
void bufferData( ulong target, Object dta, ulong usage )
	Create and initialize a buffer object's data store.
	Accepted values for usage are:
	STREAM_DRAW STATIC_DRAW DYNAMIC_DRAW
void bufferData( ulong target, long size, ulong usage )
	Set the size of a buffer object's data store.
void bufferSubData( ulong target, ulong offset, Object data )
	Update a subset of a buffer object's data store.
any getBufferParameter( ulong target, ulong value )
	Return parameter, pname, of a buffer object:
	BUFFER_SIZE BUFFER_USAGE
bool isBuffer( Object buffer )
	Determine if an object is a buffer object.
any getParameter( ulong pname )
	Relevant parameters:
	ARRAY_BUFFER_BINDING ELEMENT_ARRAY_BUFFER_BINDING
"""