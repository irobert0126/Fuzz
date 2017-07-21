import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_RENDER_BUFFER():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "createRenderbuffer"		:{
      	"api"		: None,
      	"rtn_type"	: "WebGLRenderbuffer",
      	"rtn"		: "$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==l]",
      	"arg"		: [[]]
      },
      "deleteRenderbuffer"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "bindRenderbuffer"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"g_ctx_gl.RENDERBUFFER":1},
      	    {"$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "getRenderbufferParameter"		:{
      	"api"		: None,
      	"rtn_type"	: "any",
      	"rtn"		: "",
      	"arg"		: [[
      	    {"g_ctx_gl.RENDERBUFFER":1},
      	    {"$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==r]":1}
      	]]
      },
      #void gl.renderbufferStorage(target, internalFormat, width, height);
      "renderbufferStorage"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"g_ctx_gl.RENDERBUFFER":1},
      	    {"$$[gl_rb_internalFormat]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[int??max==500]":1},
      	  ]
      	]
      },
      "isRenderbuffer"		:{
      	"api"		: None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==r]":1}
      	  ]
      	]
      },
  }
  def __init__(self):
    self.gl_rb_internalFormat= {
      "RGBA4":1,
      "RGB565":1,
      "RGB5_A1":1,
      "DEPTH_COMPONENT16":1,
      "STENCIL_INDEX8":1,
    }
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_rb_internalFormat" : {
        "impl" : self.select_gl_rb_internalFormat,
        "help" : "webgl_render_buffer",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_rb_internalFormat(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_rb_internalFormat)

"""
Object createRenderbuffer( void )
	Create a renderbuffer object
void deleteRenderbuffer( Object buffer )
	Delete a renderbuffer object.
void bindRenderbuffer( ulong target, Object buffer )
	Bind a renderbuffer, target must be RENDERBUFFER.
any getRenderbufferParameter( ulong target, ulong pname )
	Return parameter, pname, of a renderbuffer object:
		RENDERBUFFER_WIDTH
		RENDERBUFFER_HEIGHT
		RENDERBUFFER_INTERNAL_FORMAT
		RENDERBUFFER_RED_SIZE
		RENDERBUFFER_GREEN_SIZE
		RENDERBUFFER_BLUE_SIZE
		RENDERBUFFER_ALPHA_SIZE
		RENDERBUFFER_DEPTH_SIZE
		RENDERBUFFER_STENCIL_SIZE
void renderbufferStorage( ulong target, ulong format, ulong width, ulong height )
Create and initialize a renderbuffer object's data store.
	Accepted values for format are:
		RGBA4 RGB565 RGB5_A1 DEPTH_COMPONENT16 STENCIL_INDEX8
bool isRenderbuffer( Object buffer )
	Determine if an object is a renderbuffer object.
any getParameter( ulong pname )
	Relevant parameters:
		RENDERBUFFER_BINDING MAX_RENDERBUFFER_SIZE
"""