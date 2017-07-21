import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_STENCIL():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "stencilFunc" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_st_func]":1},
      	    {"$$[gl_bitplanes]":1}, #0 - 2^STENCIL_BITS
      	    {"$$[gl_bitplanes]":1},
      	  ]
      	]
      },
      "stencilFuncSeparate" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_st_face]":1},
      	    {"$$[gl_st_func]":1},
      	    {"$$[gl_bitplanes]":1}, #0 - 2^STENCIL_BITS
      	    {"$$[gl_bitplanes]":1},
      	  ]
      	]
      },
      "stencilMask" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[float??max==25535]":1},
      	  ]
      	]
      },
      "stencilMaskSeparate" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_st_face]":1},
      	    {"$$[float??max==25535]":1},
      	  ]
      	]
      },
      "stencilOp" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_st_fail]":1},
      	    {"$$[gl_st_fail]":1},
      	    {"$$[gl_st_fail]":1},
      	  ]
      	]
      },
      "stencilOpSeparate" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_st_face]":1},
      	    {"$$[gl_st_fail]":1},
      	    {"$$[gl_st_fail]":1},
      	    {"$$[gl_st_fail]":1},
      	  ]
      	]
      },
      "clearStencil" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[int??max==5]":1},
      	  ]
      	]
      },
    }
  def __init__(self):
    self.gl_st_func = {
      "NEVER":1,
      "LESS":1,
      "EQUAL":1,
      "LEQUAL":1,
      "GREATER":1,
      "NOTEQUAL":1,
      "GEQUAL":1,
      "ALWAYS":1,
    }
    self.gl_st_face = {
      "FRONT":1,
      "BACK":1,
      "FRONT_AND_BACK":1,
    }
    self.gl_st_fail = {
      "KEEP":1,
      "ZERO":1,
      "REPLACE":1,
      "INCR":1,
      "INCR_WRAP":1,
      "DECR":1,
      "DECR_WRAP":1,
      "INVERT":1,
    }
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_st_func" : {
        "impl" : self.select_gl_st_func,
        "help" : "webgl_stencil",
        "i.e." : "",
      },
      "$$[gl_bitplanes" : {
        "impl" : self.select_gl_bitplanes,
        "help" : "webgl_stencil",
        "i.e." : "",
      },
      "$$[gl_st_face" : {
        "impl" : self.select_gl_st_face,
        "help" : "webgl_stencil",
        "i.e." : "",
      },
      "$$[gl_st_fail" : {
        "impl" : self.select_gl_st_fail,
        "help" : "webgl_stencil",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_st_func(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_st_func)
  def select_gl_st_face(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_st_face)
  def select_gl_st_fail(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_st_fail)
  def select_gl_bitplanes(self, param={}):
    return "%s %% pow(2, g_ctx_gl.getParameter(g_ctx_gl.STENCIL_BITS))-1" % random.uniform(0, pow(2, 16))