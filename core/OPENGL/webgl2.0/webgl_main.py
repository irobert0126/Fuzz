import os, sys, random

sys.path.append(os.path.join(os.getcwd(), "core", "OPENGL"))
import gl__main, webgl_api_gen, webgl_buffer, webgl_type

#-----------------------------------------------------------------------#
# Concrete factories:
class GL_Web2(gl__main.GLFactory):
  def make_gl_buffer(self):
     return webgl_buffer.GL_BUFFER()
  def make_gl_api_gen(self):
     return webgl_api_gen.GL_API_GEN()
  def make_gl_type(self):
     return webgl_type.GL_TYPE()
  def make_gl_tag(self):
     return {
        "webgl_type"			:"GL_TYPE",
        "webgl_api_gen"			:"GL_API_GEN",
        "webgl_buffer"			:"GL_BUFFER",
        "webgl_frame_buffer"	:"GL_FRAME_BUFFER",
        "webgl_render_buffer"	:"GL_RENDER_BUFFER",
        "webgl_depth_buffer"	:"GL_DEPTH_BUFFER",
        "webgl_texture"			:"GL_TEXTURE",
        "webgl_culling"			:"GL_CULLING",
        "webgl_blend"			:"GL_BLENDING",
        "webgl_stencil"			:"GL_STENCIL",
        "webgl_type"			:"GL_TYPE",
        "webgl_canvas"			:"CanvasRenderingContext2D",
      }
#-----------------------------------------------------------------------#