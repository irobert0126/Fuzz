import sys, os
#-----------------------------------------------------------------------#
# The Abstract Factory:
class GLFactory:
    def make_gl_buffer(self):   pass
    def make_gl_api_gen(self):   pass
    def make_gl_tag(self):   pass
    
# Anyone who wants to access OPENGL APIs
# should ONLY use this file. 
# Other details should not be exposed.
class GLEnvironment():
  def __init__(self, factory):
    self.factory = factory
    
  def get_gl_buffer(self):
    return self.factory.make_gl_buffer()    
  def get_gl_api_gen(self):
    return self.factory.make_gl_api_gen()
  def get_gl_tag(self):
    return self.factory.make_gl_tag()
  def get_gl_type(self):
    return self.factory.make_gl_type()
    
# How Consumer access js APIs.
def factory_unit_test(environment):
  #environment.get_gl_buffer().unit_test()
  environment.get_gl_api_gen().unit_test()
  
if __name__ == "__main__":
  sys.path.append(os.path.join(os.getcwd(), "core", "OPENGL", "webgl2.0"))
  module = importlib.import_module("webgl_main")
  my_env = GLEnvironment(module.GL_Web2())
  factory_unit_test(my_env)
