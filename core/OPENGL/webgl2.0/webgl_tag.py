# Collect Template Tags Defined For WebGL

import importlib

class GL_TAG:
  def __init__(self, moduleNames=None):
    self.tags = {}
    
    if not moduleNames:
      moduleNames = {
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
        "opengl_api"			:"OPENGL_API",
      }
    for m_name, c_name in moduleNames.iteritems():
      module = importlib.import_module(m_name)
      obj = getattr(module, c_name)
      self.tags.update(obj().get_template_tag())
    