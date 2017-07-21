import random, os, sys
sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_OBJ():
  def __init__(self, api_def=None):
    self.api_def = api_def
    self.gl_objs = {}
    self.init_rtn_objs(self.api_def)

  def init_rtn_objs(self, api_def):
    if not api_def:
       return
    for api in api_def:
      print api