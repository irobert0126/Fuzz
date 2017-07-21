import random, os, sys

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_CULLING():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "cullFace" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_cl_culling_mode]":1},
      	  ]
      	]
      },
      "frontFace" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [
      	  [
      	    {"$$[gl_cl_winding_ori]":1},
      	  ]
      	]
      },
    }
      
  def __init__(self):
    self.gl_cl_culling_mode = {
      "FRONT":1,
      "BACK":1,
      "FRONT_AND_BACK":1,
    }
    self.gl_cl_winding_ori = {
      "CW":1,
      "CCW":1,
    }    
  #=================================================================================#
  def get_template_tag(self):
    return {
      "$$[gl_cl_culling_mode" : {
        "impl" : self.select_gl_cl_culling_mode,
        "help" : "webgl_culling",
        "i.e." : "",
      },
      "$$[gl_cl_winding_ori" : {
        "impl" : self.select_gl_cl_winding_ori,
        "help" : "webgl_culling",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def select_gl_cl_culling_mode(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_cl_culling_mode)
  def select_gl_cl_winding_ori(self, param={}):
    return "g_ctx_gl." + util.w_choice(self.gl_cl_winding_ori)