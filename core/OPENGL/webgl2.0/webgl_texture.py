import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_TEXTURE():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "createTexture" :{
      	"api"		: None,
      	"rtn_type"	: "WebGLTexture",
      	"rtn"		: "$$[GL_OBJ??type==WebGLTexture&&LorR==l]",
      	"arg"		: [[]]
      },
      "deleteTexture" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[GL_OBJ??type==WebGLTexture&&LorR==r]":1},
      	  ]
      	]
      },
      "bindTexture" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_tt_texturing_target]":1},
      	    {"$$[GL_OBJ??type==WebGLTexture&&LorR==r]":1},
      	  ]
      	]
      },
      "activeTexture" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[int??max==5]+8":1},
      	    #  0 to gl.MAX_COMBINED_TEXTURE_IMAGE_UNITS - 1
      	  ]      	 
      	],
      	"arg_spec": 1
      },
      "texParameterf" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_tt_texturing_target]":1},
      	    {"$$[gl_tt_texture_pname]":1},
      	    {"$$[gl_tt_texture_param]":1},
      	  ]
      	],
      	#The value of param depends on the value of pname.
      	"arg_spec": 1
      },
      "texParameteri" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_tt_texturing_target]":1},
      	    {"$$[gl_tt_texture_pname]":1},
      	    {"$$[gl_tt_texture_param]":1},
      	  ]
      	],
      	# TODO:
      	#The value of param depends on the value of pname.
      	#https://msdn.microsoft.com/en-us/library/dn302437(v=vs.85).aspx
      	"arg_spec": 1
      },
      "texImage2D" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_tt_active_texture_target]":1},
      	    {"$$[int??max==2]":1},
      	    {"$$[gl_tt_texture_color]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[int??max==500]":1},
      	    {"0":1},
      	    {"$$[gl_tt_texture_color]":1},
      	    {"$$[gl_tt_texture_type]":1},
      	    {"$$[GL_OBJ??type==ArrayBufferView||ImageData||HTMLImageElement||HTMLCanvasElement||HTMLVideoElement&&LorR==r]":1},
      	  ],
      	  [  #texImage2D( ulong target, long level, Object data,
      	     #            [bool flipY], [bool asPreMultipliedAlpha] )
      	    {"$$[gl_tt_active_texture_target]":1},
      	    {"$$[int??max==2]":1},
      	    {"$$[GL_OBJ??type==ArrayBufferView||ImageData||HTMLImageElement||HTMLCanvasElement||HTMLVideoElement&&LorR==r]":1},
      	    {"$$[bool]":0},
      	    {"$$[bool]":0},
      	  ]
      	]
      },      
      "texSubImage2D" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [ # void gl.texImage2D(target, level, xoffset, yoffset, 
      	    #                    width, height, format, type, ArrayBufferView? pixels);
      	    {"$$[gl_tt_active_texture_target]":1},
      	    {"$$[int??max==2]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[gl_tt_texture_color]":1},
      	    {"$$[gl_tt_texture_type]":1},
      	    {"$$[GL_OBJ??type==ArrayBufferView||ImageData||HTMLImageElement||HTMLCanvasElement||HTMLVideoElement&&LorR==r]":1},
      	  ],
      	  [  # void gl.texImage2D(target, level, xoffset, yoffset, 
      	     #                    format, type, ImageData? pixels);
      	    {"$$[gl_tt_active_texture_target]":1},
      	    {"$$[int??max==2]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[gl_tt_texture_color]":1},
      	    {"$$[gl_tt_texture_type]":1},
      	    {"$$[GL_OBJ??type==ArrayBufferView||ImageData||HTMLImageElement||HTMLCanvasElement||HTMLVideoElement&&LorR==r]":1},
      	  ]
      	]
      }, 
      "copyTexImage2D" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [ # copyTexImage2D( ulong target, long level, ulong intformat, 
      	    #                    long x, long y, ulong width, ulong height, long border )
      	    {"$$[gl_tt_active_texture_target]":1},
      	    {"$$[int??max==2]":1},
      	    {"$$[gl_tt_texture_color]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[int??max==500]":1},
      	    {"0":1},
      	  ],
      	]
      },
      "copyTexSubImage2D" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [ # copyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height);
      	    {"$$[gl_tt_active_texture_target]":1},
      	    {"$$[int??max==2]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==100]":1},
      	    {"$$[int??max==500]":1},
      	    {"$$[int??max==500]":1},
      	  ],
      	]
      },
      "generateMipmap" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [ # generateMipmap(target);
      	    {"$$[gl_tt_active_texture_target]":1},
      	  ],
      	]
      },
      "isTexture" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [ # isTexture(buffer);
      	    {"$$[GL_OBJ??type==WebGLTexture&&LorR==r]":1},
      	  ],
      	]
      },
    }
  def __init__(self):
    self.gl_tt_texturing_target = {
      "TEXTURE_2D":1,
      "TEXTURE_CUBE_MAP":1,
    }
    self.gl_tt_texture_pname = {
      "TEXTURE_MIN_FILTER":1,
      "TEXTURE_MAG_FILTER":1,
      "TEXTURE_WRAP_S":1,
      "TEXTURE_WRAP_T":1,
      "TEXTURE_MAX_ANISOTROPY_EXT":1,
    }
    self.gl_tt_texture_param = {
      "LINEAR":1,
      "NEAREST":1,
      "LINEAR_MIPMAP_LINEAR":1,
      "LINEAR_MIPMAP_NEAREST":1,
      "NEAREST_MIPMAP_LINEAR":1,
      "NEAREST_MIPMAP_NEAREST":1,
      "CLAMP_TO_EDGE":1,
      "REPEAT":1,
      "MIRRORED_REPEAT":1,
      "CLAMP_TO_EDGE":1,
    }
    self.gl_tt_active_texture_target = {
      "TEXTURE_2D":1,
      "TEXTURE_CUBE_MAP_POSITIVE_X":1,
      "TEXTURE_CUBE_MAP_NEGATIVE_X":1,
      "TEXTURE_CUBE_MAP_POSITIVE_Y":1,
      "TEXTURE_CUBE_MAP_NEGATIVE_Y":1,
      "TEXTURE_CUBE_MAP_POSITIVE_Z":1,
      "TEXTURE_CUBE_MAP_NEGATIVE_Z":1,
    }
    self.gl_tt_texture_color = {
      "ALPHA":1,
      "LUMINANCE":1,
      "LUMINANCE_ALPHA":1,
      "RGB":1,
      "RGBA":1,
    }
    self.gl_tt_texture_type = {
      "UNSIGNED_BYTE":1,
      "FLOAT":1,
      "UNSIGNED_SHORT_5_6_5":1,
      "UNSIGNED_SHORT_4_4_4_4":1,
      "UNSIGNED_SHORT_5_5_5_1":1,
    }
 
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_tt_texturing_target" : {
        "impl" : self.select_gl_tt_texturing_target,
        "help" : "webgl_texture",
        "i.e." : "",
      },
      "$$[gl_tt_texture_pname" : {
        "impl" : self.select_gl_tt_texture_pname,
        "help" : "webgl_texture",
        "i.e." : "",
      },
      "$$[gl_tt_texture_param" : {
        "impl" : self.select_gl_tt_texture_param,
        "help" : "webgl_texture",
        "i.e." : "",
      },
      "$$[gl_tt_texture_color" : {
        "impl" : self.select_gl_tt_texture_color,
        "help" : "webgl_texture",
        "i.e." : "",
      },
      "$$[gl_tt_texture_type" : {
        "impl" : self.select_gl_tt_texture_type,
        "help" : "webgl_texture",
        "i.e." : "",
      },
      "$$[gl_tt_active_texture_target" : {
        "impl" : self.select_gl_tt_active_texture_target,
        "help" : "webgl_texture",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_tt_texturing_target(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_tt_texturing_target)
  def select_gl_tt_texture_pname(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_tt_texture_pname)
  def select_gl_tt_texture_param(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_tt_texture_param)
  def select_gl_tt_active_texture_target(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_tt_active_texture_target)
  def select_gl_tt_texture_color(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_tt_texture_color)
  def select_gl_tt_texture_type(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_tt_texture_type)
    

"""
Object createTexture( void )
	Create a texture
void deleteTexture( Object texture )
	Delete a texture.
void bindTexture( ulong target, Object texture )
	Bind a texture to a texturing target. Accepted values
	for target are:
		TEXTURE_2D TEXTURE_CUBE_MAP
void activeTexture( ulong texture )
	Select active texture unit.
any getTexParameter( ulong target, ulong pname )
	Return parameter, pname, of a texture:
		TEXTURE_WRAP_S TEXTURE_MAG_FILTER
		TEXTURE_WRAP_T TEXTURE_MIN_FILTER
void texParameterf( ulong target, ulong pname, float v )
void texParameteri( ulong target, ulong pname, long v )
	Set texture parameters.
void texImage2D( ulong target, long level, ulong intformat, ulong width, ulong height, long border, ulong format, ulong type, Object data )
	Specify a two-dimensional texture image from a
	WebGLArray of pixel data. See readPixels for accepted
	type values. Accepted values for intformat and format are:
		ALPHA RGB RGBA LUMINANCE LUMINANCE_ALPHA
void texImage2D( ulong target, long level, Object data, [bool flipY], [bool asPreMultipliedAlpha] )
	Specify a two-dimensional texture image from either
	an ImageData object or a HTMLImageElement, HTMLCanvasElement or HTMLVideoElement.
void texSubImage2D( ulong target, long level,
long xoffset, long yoffset, ulong width, ulong
height, ulong format, ulong type, Object data )
Specify a two-dimensional texture subimage from a
WebGLArray of pixel data.
void texSubImage2D( ulong target, long level,
long xoffset, long yoffset, Object data, [bool
flipY], [bool asPreMultipliedAlpha] )
Specify a two-dimensional texture subimage from
either an ImageData object or a HTMLImageElement,
HTMLCanvasElement or a HTMLVideoElement.
void copyTexImage2D( ulong target, long level,
ulong intformat, long x, long y, ulong width,
ulong height, long border )
Copy pixels into a 2D texture image. See
framebufferTexture2D for accepted target values.
void copyTexSubImage2D( ulong target, long level,
ulong intformat, long xoffset, long yoffset, long
x, long y, ulong width, ulong height )
Copy a two-dimensional texture subimage.
void generateMipmap( ulong target )
Generate a complete set of mipmaps for a texture.
bool isTexture( Object buffer )
Determine if an object is a texture.
any getParameter( ulong pname )
Relevant parameters:
TEXTURE_BINDING_2D
TEXTURE_BINDING_CUBE_MAP
MAX_TEXTURE_SIZE
MAX_CUBE_MAP_TEXTURE_SIZE
ACTIVE_TEXTURE
MAX_TEXTURE_IMAGE_UNITS
MAX_VERTEX_TEXTURE_IMAGE_UNITS
MAX_COMBINED_TEXTURE_IMAGE_UNITS
"""