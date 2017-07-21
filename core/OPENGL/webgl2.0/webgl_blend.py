import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_BLENDING():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "blendFunc" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_bl_factor]":1},
      	  ]
      	]
      },
      "blendFuncSeparate" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_bl_factor]":1},
      	    {"$$[gl_bl_factor]":1},
      	    {"$$[gl_bl_factor]":1},
      	    {"$$[gl_bl_factor]":1},
      	  ]
      	]
      },
      "blendEquation" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_bl_equation]":1},
      	  ]
      	]
      },
      "blendEquationSeparate" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_bl_equation]":1},
      	    {"$$[gl_bl_equation]":1},
      	  ]
      	]
      },
      "blendColor" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[float??max==1]":1},
      	    {"$$[float??max==1]":1},
      	    {"$$[float??max==1]":1},
      	    {"$$[float??max==1]":1},
      	  ]
      	]
      },
    }
  def __init__(self):
    self.gl_bl_factor = {
      "ZERO":1,
      "ONE":1,
      "SRC_COLOR":1,
      "ONE_MINUS_SRC_COLOR":1,
      "DST_COLOR":1,
      "ONE_MINUS_DST_COLOR":1,
      "SRC_ALPHA":1,
      "ONE_MINUS_SRC_ALPHA":1,
      "DST_ALPHA":1,
      "ONE_MINUS_DST_ALPHA":1,
      "SRC_ALPHA_SATURATE":1,
    }
    self.gl_bl_equation = {
      "FUNC_ADD":1,
      "FUNC_SUBTRACT":1,
      "FUNC_REVERSE_SUBTRACT":1,
    }
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_bl_factor" : {
        "impl" : self.select_gl_bl_factor,
        "help" : "webgl_blend",
        "i.e." : "",
      },
      "$$[gl_bl_equation" : {
        "impl" : self.select_gl_bl_equation,
        "help" : "webgl_blend",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_bl_factor(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_bl_factor)
  def select_gl_bl_equation(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_bl_equation)