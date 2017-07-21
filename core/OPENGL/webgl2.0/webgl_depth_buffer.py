import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_DEPTH_BUFFER():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "depthFunc"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_db_depth_func]":1},
      	  ]
      	]
      },
      "depthMask"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[bool]":1},
      	  ]
      	]
      },
      "depthRange"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[float??max==1]":1},
      	    {"$$[float??max==1]":1},
      	  ]
      	]
      },
      "clearDepth"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[int??max==1]":1},
      	  ]
      	]
      },
      "polygonOffset"		:{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[int??max==3]":1},
      	  ]
      	]
      },
  }
  
  def __init__(self):
    self.gl_db_depth_func = {
      "NEVER":1,
      "LESS":1,
      "EQUAL":1,
      "LEQUAL":1,
      "GREATER":1,
      "NOTEQUAL":1,
      "GEQUAL":1,
      "ALWAYS":1,
    }
 
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_db_depth_func" : {
        "impl" : self.select_gl_db_depth_func,
        "help" : "webgl_depth_buffer",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_db_depth_func(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_db_depth_func)
    