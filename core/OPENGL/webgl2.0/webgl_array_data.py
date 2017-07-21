
class GL_DRAW_ARRAY():
  caller = {
    "$$[GL_OBJ??type==WebGLRenderingContext&&LorR==r]":1,
  }
  api = {
      "clear" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [ [ ] ]
      },
      "flush" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [ [ ] ]
      },
      "finish" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [ [ ] ]
      },
      # TODO: Valid draw, need to allocate array first
      "drawElements" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [ [
      	    {"g_ctx_gl.$$[draw_array_mode]":1},
      	    {"$$[int??max==50]":1},
      	    {"g_ctx_gl.UNSIGNED_BYTE":1},
      	    {"0":1},
      	] ]
      },
      "drawArrays" :{
      	"api"		: None,
      	"rtn_type"	: "void",
      	"rtn"		: "",
      	"arg"		: [ [
      	    {"g_ctx_gl.$$[draw_array_mode]":1},
      	    {"$$[int??max==50]":1},
      	    {"g_ctx_gl.UNSIGNED_BYTE":1},
      	    {"0":1},
      	] ]
      },
      
  def __init__(self): 
    self.draw_array_mode = {
      "POINTS"			:1,
      "LINES"			:1,
      "LINE_STRIP"		:1,
      "LINE_LOOP"		:1,
      "TRIANGLES"		:1,
      "TRIANGLE_STRIP"	:1,
      "TRIANGLE_FAN"	:1,
    }
    self.unknown = {
      "ARRAY_BUFFER"			:1,
      "ELEMENT_ARRAY_BUFFER"	:1, 
      "COPY_READ_BUFFER"		:1, 
      "COPY_WRITE_BUFFER"		:1, 
      "PIXEL_UNPACK_BUFFER"		:1, 
      "PIXEL_PACK_BUFFER"		:1, 
      "QUERY_BUFFER"			:1, 
      "TEXTURE_BUFFER"			:1, 
      "TRANSFORM_FEEDBACK_BUFFER":1, 
      "UNIFORM_BUFFER"			:1, 
      "DRAW_INDIRECT_BUFFER"	:1, 
      "ATOMIC_COUNTER_BUFFER"	:1, 
      "DISPATCH_INDIRECT_BUFFER":1, 
      "SHADER_STORAGE_BUFFER"	:1,
	}

  def get_template_tag(self):
    return {
      "$$[draw_array_mode" : {
        "impl" : self.fill_draw_arrays_mode,
        "help" : "webgl_array_data",
        "i.e." : "",
      },
      "$$[" : {
        "impl" : self.,
        "help" : "webgl_array_data",
        "i.e." : "",
      },
    }
  #=================================================================================#
  def fill_draw_arrays_mode():
    return util.w_choice(self.draw_array_mode)
  #=================================================================================#
  def block_drawArrays_valid(self, gl="g_ctx_gl", buffer = None):
    if not buffer:
      buffer = "%s.%s" % (gl, self.api_createBuffer())
    statement_temp = [
	  "var vertex_index = $$[int??max==9];",
	  "%s.%s;" % (gl, self.api_bindBuffer(gl=gl, target="ARRAY_BUFFER", buffer=buffer)),
	  "%s.%s;" % (gl, self.api_bufferData(data_or_size="new Float32Array(vertices_array[vertex_index])")),
	  "%s.drawArrays  (%s.$$[draw-arrays-mode], 0, vertex_index);" % (gl, gl),
	]
    return "\n".join(statement_temp)

  def block_drawArrays_random(self, gl="g_ctx_gl", buffer = None):
    if not buffer:
      buffer = "%s.%s" % (gl, self.api_createBuffer())
    statement_temp = [
	  "var vertex_index = $$[int??max==9];",
	  "%s.%s;" % (gl, self.api_bindBuffer(gl=gl, buffer=buffer)),
	  "%s.%s;" % (gl, self.api_bufferData(data_or_size="new Float32Array(vertices_array[vertex_index])")),
	  "%s.drawArrays  (%s.$$[draw-arrays-mode], 0, vertex_index);" % (gl, gl),
	]
    return "\n".join(statement_temp)

  def block_drawElements_valid(self, gl="g_ctx_gl", buffer = None):
    if not buffer:
      buffer = "%s.%s" % (gl, self.api_createBuffer())
    statement_temp = [
	  "var indice_index = $$[int??max==9];",
	  "%s.%s;" % (gl, self.api_bindBuffer(gl=gl, target="ELEMENT_ARRAY_BUFFER", buffer=buffer)),
	  "%s.%s;" % (gl, self.api_bufferData(
	   				target="ELEMENT_ARRAY_BUFFER",
	  				data_or_size="new Float32Array(indices_array[indice_index])")
	  			 ),
	  "%s.drawElements(%s.$$[draw-arrays-mode], indice_index, %s.UNSIGNED_SHORT, 0);" % (gl, gl, gl),
	]
    return "\n".join(statement_temp)

  def fill_block_drawElements_random(self, gl="g_ctx_gl", buffer = None):
    if not buffer:
      buffer = "%s.%s" % (gl, self.api_createBuffer())
    statement_temp = [
	  "var indice_index = $$[int??max==9];",
	  "%s.%s;" % (gl, self.api_bindBuffer(gl=gl, buffer=buffer)),
	  "%s.%s;" % (gl, self.api_bufferData(
	  				data_or_size="new Float32Array(indices_array[indice_index])")
	  			 ),
	  "%s.drawElements(%s.$$[draw-arrays-mode], indice_index, %s.UNSIGNED_SHORT, 0);" % (gl, gl, gl),
	]
    return "\n".join(statement_temp)
    
  #=======================================================================================

  def unit_test(self):
    print "\n[+] WEBGL block_drawArrays_valid Test:"
    print self.block_drawArrays_valid(), "\n"
    print "[+] WEBGL block_drawElements_valid Test:"
    print self.block_drawElements_valid(), "\n"