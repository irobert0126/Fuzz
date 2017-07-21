import os, sys, random
import opengl_env, opengl_api, opengl_var

class OpenGL():
  def __init__(self):
    self.opengl_env = opengl_env.env()
    self.opengl_api = opengl_api.OpenGL_API(self.opengl_env)
    self.opengl_var = opengl_var.opengl_var(self.opengl_env)
    
    self.vertex_body = []
    self.frag_body = []

  def generate_vertex(self):
    for i in range(1, 2):
      self.vertex_body.append(self.opengl_api.generate_function({"state":"vertex"}))

  def dump_vertex(self):
    shared = self.get_runtime_env().dump_shared()
    vertex_build_in = self.get_runtime_env().fill_build_in({"state":"vertex"})
    vertex_decl = self.get_runtime_env().dump_declaration({"state":"vertex"})
    return "\t\n".join([vertex_decl, shared, "void main(void){", "\t\t\n".join(self.vertex_body), vertex_build_in,"}"])

  def generate_fragment(self):
    for i in range(1, 2):
      self.frag_body.append(self.opengl_api.generate_function({"state":"fragment"}))

  def dump_fragment(self):
    shared = self.get_runtime_env().dump_shared()
    frag_build_in = self.get_runtime_env().fill_build_in({"state":"fragment"})
    frag_decl = self.get_runtime_env().dump_declaration({"state":"fragment"})
    return "\t\n".join([frag_decl, shared, "void main(void){", "\t\t\n".join(self.frag_body), frag_build_in, "}"])

  def gen_shader(self, params):
    self.generate_vertex()
    self.generate_fragment()
    return "\t\n".join(
      ['<script id="shader-vs" type="x-shader/x-vertex">',
       self.dump_vertex(),
       '</script>',
       '<script id="shader-fs" type="x-shader/x-fragment">',
       self.dump_fragment(),
       '</script>'])

  def get_runtime_env(self):
    return self.opengl_env

  def get_template_tag(self):
    return {
      "$$[shader" : {
        "impl" : self.gen_shader,
        "help" : "",
        "i.e." : "",
      }
    }

if __name__ == "__main__":
  opengl = OpenGL()
  vertex_body = []
  for i in range(1, 100):
    vertex_body.append(opengl.opengl_api.generate_function({"state":"vertex"}))
  vertex_build_in = opengl.get_runtime_env().fill_build_in({"state":"vertex"})
  
  frag_body = []
  for i in range(1, 100):
    frag_body.append(opengl.opengl_api.generate_function({"state":"fragment"}))
  frag_build_in = opengl.get_runtime_env().fill_build_in({"state":"fragment"})
    
  shared = opengl.get_runtime_env().dump_shared()
  vertex_decl = opengl.get_runtime_env().dump_declaration({"state":"vertex"})
  frag_decl = opengl.get_runtime_env().dump_declaration({"state":"fragment"})
  print vertex_decl, "\n\n", shared, "\n\nmain(){\n", "\n".join(vertex_body), "\n", vertex_build_in,"}\n\n\n"
  print frag_decl, "\n\n", shared, "\n\nmain(){\n", "\n".join(frag_body), "\n", frag_build_in,"}\n\n\n"