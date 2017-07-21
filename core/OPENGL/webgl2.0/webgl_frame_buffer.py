import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_FRAME_BUFFER():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "createFramebuffer"		:{
      	"api": None,
      	"rtn_type"	: "WebGLFramebuffer",
      	"rtn"		: "$$[GL_OBJ??type==WebGLFramebuffer&&LorR==l]",
      	"arg": [[]]
      },
      "deleteFramebuffer"		:{
      	"api": None,
      	"rtn_type": "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[GL_OBJ??type==WebGLFramebuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "bindFramebuffer"			:{
      	"api": None,
      	"rtn_type": "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"g_ctx_gl.FRAMEBUFFER":1},
      	    {"$$[GL_OBJ??type==WebGLFramebuffer&&LorR==r]":1}
      	  ]
      	]      	
      },
      "checkFramebufferStatus"	:{
      	"api": None,
      	"rtn_type": "ulong",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"g_ctx_gl.FRAMEBUFFER":1}
      	  ]
      	]
      },
      "framebufferRenderbuffer"	:{
      	"api": None,
      	"rtn_type": "ulong",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"g_ctx_gl.FRAMEBUFFER":1},
      	    {"$$[gl_fb_attachment]":1},
      	    {"g_ctx_gl.RENDERBUFFER":1},
      	    {"$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "framebufferTexture2D"	:{
      	"api": None,
      	"rtn_type": "ulong",
      	"rtn"	  : "",
      	"arg": [
      	  [
      	    {"g_ctx_gl.FRAMEBUFFER":1},
      	    {"$$[gl_fb_attachment]":1},
      	    {"$$[gl_fb_textarget]":1},
      	    {"$$[GL_OBJ??type==WebGLTexture&&LorR==r]":1},
      	    {"0":1}
      	  ]
      	]
      },
      "pixelStorei"				:{
      	"api": None,
      	"rtn_type": "void",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[gl_fb_pixel_storage]":1},
      	    {"1":1},
      	  ]
      	]
      },
      "readPixels"				:{
      	"api": None,
      	"rtn": "Array",
      	"rtn"		: "",
      	"arg": [
      	  [
        	{"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[gl_fb_pixel_format]":1},
      	    {"$$[gl_fb_pixel_type_2_data]":1}, 
      	  ]
      	]
      },
      "isFramebuffer"			:{
      	"api": None,
      	"rtn_type"	: "bool",
      	"rtn"		: "",
      	"arg": [
      	  [
      	    {"$$[GL_OBJ??type==WebGLRenderbuffer&&LorR==r]":1}
      	  ]
      	]
      },
      "getFramebufferAttachmentParameter"	:{
      	"api": None,
      	"rtn_type": "any",
      	"rtn"		: "",
      	"arg": [[]]
      }
  }
  def __init__(self):
    ###########################################################
    self.gl_fb_attachment = {
      "COLOR_ATTACHMENT0":1,
      "DEPTH_ATTACHMENT":1,
      "STENCIL_ATTACHEMENT":1,
      "DEPTH_STENCIL_ATTACHEMENT":1,
    }
    self.gl_fb_textarget = {
      "TEXTURE_2D":1,
      "TEXTURE_CUBE_MAP_POSITIVE_X":1,
      "TEXTURE_CUBE_MAP_NEGATIVE_X":1,
      "TEXTURE_CUBE_MAP_POSITIVE_Y":1,
      "TEXTURE_CUBE_MAP_NEGATIVE_Y":1,
      "TEXTURE_CUBE_MAP_POSITIVE_Z":1,
      "TEXTURE_CUBE_MAP_NEGATIVE_Z":1,
    }
    self.gl_fb_pixel_storage = {
      "PACK_ALIGNMENT":1,
      "UNPACK_ALIGNMENT":1,
      "UNPACK_FLIP_Y_WEBGL":1,
      "UNPACK_PREMULTIPLY_ALPHA_WEBGL":1,
      "UNPACK_COLORSPACE_CONVERSION_WEBGL":1,
    }
    self.gl_fb_pixel_format= {
      "ALPHA":1,
      "RGB":1,
      "RGBA":1,
    }
    self.gl_fb_pixel_data_type= {
      "UNSIGNED_BYTE":1,
      "UNSIGNED_SHORT_5_6_5":1,
      "UNSIGNED_SHORT_4_4_4_4":1,
      "UNSIGNED_SHORT_5_5_5_1":1,
      "FLOAT":1,
    }
    self.gl_fb_pixel_type_TO_data= {
      # LorR=l is because read data to this Array
      "UNSIGNED_BYTE"			: "$$[GL_OBJ??type==Uint8Array&&LorR==l]",
      "UNSIGNED_SHORT_5_6_5"	: "$$[GL_OBJ??type==Uint16Array&&LorR==l]",
      "UNSIGNED_SHORT_4_4_4_4"	: "$$[GL_OBJ??type==Uint16Array&&LorR==l]",
      "UNSIGNED_SHORT_5_5_5_1"	: "$$[GL_OBJ??type==Uint16Array&&LorR==l]",
      "FLOAT"					: "$$[GL_OBJ??type==Float32Array&&LorR==l]",
    }
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_fb_attachment" : {
        "impl" : self.select_gl_fb_attachment,
        "help" : "webgl_frame_buffer",
        "i.e." : "",
      },
      "$$[gl_fb_textarget" : {
        "impl" : self.select_gl_fb_textarget,
        "help" : "webgl_frame_buffer",
        "i.e." : "",
      },
      "$$[gl_fb_pixel_storage" : {
        "impl" : self.select_gl_fb_pixel_storage,
        "help" : "webgl_frame_buffer",
        "i.e." : "",
      },
      "$$[gl_fb_pixel_format" : {
        "impl" : self.select_gl_fb_pixel_format,
        "help" : "webgl_frame_buffer",
        "i.e." : "",
      },
      "$$[gl_fb_pixel_data_type" : {
        "impl" : self.select_gl_fb_pixel_data_type,
        "help" : "webgl_frame_buffer",
        "i.e." : "",
      },
      "$$[gl_fb_pixel_type_2_data" : {
        "impl" : self.select_gl_fb_pixel_type_AND_data,
        "help" : "webgl_frame_buffer",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_fb_attachment(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_fb_attachment)
  def select_gl_fb_textarget(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_fb_textarget)
  def select_gl_fb_pixel_storage(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_fb_pixel_storage)
  def select_gl_fb_pixel_format(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_fb_pixel_format)        
  def select_gl_fb_pixel_data_type(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_fb_pixel_data_type) 
    
  def select_gl_fb_pixel_type_AND_data(self, param={}):  
    pixel_data_type = self.select_gl_fb_pixel_data_type(param)
    data = self.gl_fb_pixel_type_TO_data[pixel_data_type.split(".")[-1]]
    return "%s, %s" % (pixel_data_type, data)
  #=================================================================================#
"""
Object createFramebuffer( void )
	Create a framebuffer object
void deleteFramebuffer( Object buffer )
	Delete a framebuffer object.
void bindFramebuffer( ulong target, Object buffer )
	Bind a framebuffer, target must be FRAMEBUFFER.
ulong checkFramebufferStatus( ulong target )
	Return the framebuffer completeness status of a framebuffer object.
	Return values are:
		FRAMEBUFFER_COMPLETE
		FRAMEBUFFER_INCOMPLETE_ATTACHMENT
		FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT
		FRAMEBUFFER_INCOMPLETE_DIMENSIONS
		FRAMEBUFFER_UNSUPPORTED
ulong framebufferRenderbuffer( ulong target, ulong att, ulong rbtarget, Object rbuffer )
	Attach a renderbuffer object to a framebuffer object.
	Accepted values for attachment are:
		DEPTH_ATTACHMENT COLOR_ATTACHMENT0
		STENCIL_ATTACHMENT
any getFramebufferAttachmentParameter(ulong target, ulong attachment, ulong pname)
	Return attachment parameters of a framebuffer object.
	Accepted values for attachment are:
		FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE
		FRAMEBUFFER_ATTACHMENT_OBJECT_NAME
		FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL
		FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE
ulong framebufferTexture2D( ulong target, ulong att, ulong textarget, Object tex, ulong level )
	Attach a texture image to a framebuffer object.
	Accepted values for textarget are:
		TEXTURE_2D
		TEXTURE_CUBE_MAP_POSITIVE_X
		TEXTURE_CUBE_MAP_NEGATIVE_X
		TEXTURE_CUBE_MAP_POSITIVE_Y
		TEXTURE_CUBE_MAP_NEGATIVE_Y
		TEXTURE_CUBE_MAP_POSITIVE_Z
		TEXTURE_CUBE_MAP_NEGATIVE_Z
void pixelStorei( ulong pname, long param )
	Set pixel storage modes. Accepted pname values are:
		PACK_ALIGNMENT UNPACK_ALIGNMENT
Array readPixels( long x, long y, ulong width, ulong height, ulong format, ulong type )
	Read a block of pixels from the frame buffer. Accepted
	format values are:
		ALPHA RGB RGBA
	Accepted type values are:
		UNSIGNED_BYTE
		UNSIGNED_SHORT_4_4_4_4
		UNSIGNED_SHORT_5_5_5_1
		UNSIGNED_SHORT_5_6_5
bool isFramebuffer( Object buffer )
	Determine if an object is a framebuffer object.
"""
