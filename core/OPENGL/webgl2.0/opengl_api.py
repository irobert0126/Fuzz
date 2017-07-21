import random

class OpenGL_API:
  def __init__(self, env):
    self.env = env
    self.precision = ["highp", "mediump", "lowp"]

    self.types_basic = ["float", "int", "void", "bool"]
    self.types_vector = ["vec2", "vec3", "vec4", "ivec2", "ivec3", "ivec4", "bvec2", "bvec3", "bvec4"]
    self.types_matrix = ["mat2", "mat3", "mat4"]
    self.types_sampler = ["sampler2D", "samplerCube"]
    
    # ["textureCube",
    self.texture_function = ["texture2D","texture2DLod","textureCubeLod", "texture2DProj","texture2DProjLod"]
    self.matrix_function = ["matrixCompMult"]
    self.geometric_function = ["length","distance","dot","cross","normalize","faceforward", "reflect", "refract"]
    self.common_function = ["abs","sign","floor","ceil","fract","mod","min","max","clamp","mix","step","smoothstep"]
    self.exponential_function = ["pow","exp","log","exp2","log2","sqrt","inversesqrt"]
    self.buildin_functions = {}
    self.buildin_functions["any"] = []
    self.buildin_functions["any"].extend(self.texture_function + self.matrix_function + self.geometric_function + self.common_function + self.exponential_function)
    self.buildin_functions["ver"] = ["texture2DLod", "texture2DProjLod", "textureCubeLod"]
    self.buildin_functions["frag"] = [""]
    self.static_return_type = {
      "length":["float"],       "distance":["float"],         "dot":["float"],          "cross":["vec3"],    
      "texture2DLod":["vec4"],  "texture2DProjLod":["vec4"],  "textureCubeLod":["vec4"],
      "texture2D":["vec4"],     "texture2DProj":["vec4"],     "textureCube":["vec4"],
      "matrixCompMult":self.types_matrix,
    }
  #=================================================================#     
  def generate_statement(self, params={}):
    l_param = {"state":params["state"], "qualifier":"local", "lorr":"left"}
    r_param = {"state":params["state"], "lorr":"left"}
    return "%s = %s;" % (self.env.pick_variable(l_param), self.env.fill_variable_value(r_param))
       
  def generate_function(self, params={}):
    if not params:
      params = {}
    if "state" not in params:
      params["state"] = "any"
    if "name" not in params:
      params["name"] = self.choose_a_function_name(params["state"])
        
    rtn_type, func_body = self.fill_simple_function(params)
    rtn_param = {"state":params["state"], "qualifier":"local", "type":rtn_type, "lorr":"left"}
    l_value = self.env.pick_variable(rtn_param)
    return "%s = %s;" % (l_value, func_body)
    				   
  def choose_a_function_name(self, state):
    while True:
      name = random.choice(self.buildin_functions["any"])
      if state == "vertex" and name not in self.buildin_functions["frag"]:
        return name
      if state == "fragment" and name not in self.buildin_functions["ver"]:
        return name
      if state == "any":
        return name
  #=================================================================#
  def get_float_value(self):
    return "%s%s.%s" % (random.choice([" -",""]), random.randint(0, 100000), random.randint(0, 1000))
    
  def fill_simple_function(self, params):
    params["type"] = random.choice([ "float", "vec2", "vec3", "vec4" ]) if "type" not in params else params["type"]    
            
    if params["name"] in ["length","dot"]: #"distance",
      return "float", "%s(%s)" % (params["name"], self.env.fill_variable_value(params))
        
    if params["name"] in ["exp","log","exp2","log2","abs","fract","normalize","floor","sqrt","inversesqrt","sign","ceil"]:
      return params["type"], "%s(%s)" % (params["name"], self.env.fill_variable_value(params))
      
    if params["name"] in ["pow","dot","reflect"]:
      return params["type"], "%s(%s, %s)" % (params["name"],
       self.env.fill_variable_value(params),
       self.env.fill_variable_value(params))
       
    if params["name"] in ["max","mod","min"]:
      second_p = self.env.fill_variable_value(params) if random.randint(0, 1) == 0 else self.get_float_value()
      return params["type"], "%s(%s, %s)" % (params["name"], 
        self.env.fill_variable_value(params), second_p)
        
    if params["name"] in ["cross","matrixCompMult"]:
      if params["name"] == "cross":
        params["type"] = "vec3"
      if params["name"] == "matrixCompMult":
        params["type"] = random.choice([ "mat2", "mat3", "mat4" ])
      return params["type"], "%s(%s, %s)" % (params["name"], 
        self.env.fill_variable_value(params),
        self.env.fill_variable_value(params))
  
    if params["name"] in ["faceforward"]:
      return params["type"], "%s(%s, %s, %s)" % (params["name"], 
        self.env.fill_variable_value(params),
        self.env.fill_variable_value(params),
        self.env.fill_variable_value(params))
        
    if params["name"] in ["refract"]:
      return params["type"], "%s(%s, %s, %s)" % (params["name"], 
        self.env.fill_variable_value(params),
        self.env.fill_variable_value(params),
        self.get_float_value())
        
    if params["name"] == "textureCube":
      return self.function_textureCube(params)
    if params["name"] == "textureCubeLod":
      return self.function_textureCubeLod(params)
    if params["name"] == "texture2D":
      return self.function_texture2D(params)
    if params["name"] == "texture2DProj":
      return self.function_texture2DProj(params)
    if params["name"] == "texture2DLod":
      return self.function_texture2DLod(params)
    if params["name"] == "texture2DProjLod":
      return self.function_texture2DProjLod(params)
      
    if params["name"] == "clamp":
      return self.function_clamp(params)
    if params["name"] == "mix":
      return self.function_mix(params)
    if params["name"] == "smoothstep":
      return self.function_smoothstep(params)
    if params["name"] == "step":
      return self.function_step(params)
       
  def function_textureCube(self, params={}):
    temp = params["type"]
    params["type"] = "samplerCube"
    arg1 = self.env.fill_variable_value(params)
    params["type"] = "vec3"
    arg2 = self.env.fill_variable_value(params)
    params["type"] = temp
    if random.randint(1, 2) == 1:
      return "vec4", "textureCube(%s, %s)" % (arg1, arg2)
    else:
      return "vec4", "textureCube(%s, %s, %s)" % (arg1, arg2, self.get_float_value())
      
  def function_textureCubeLod(self, params={}):
    temp = params["type"]
    params["type"] = "samplerCube"
    arg1 = self.env.fill_variable_value(params)
    params["type"] = "vec3"
    arg2 = self.env.fill_variable_value(params)
    arg3 = self.get_float_value()
    params["type"] = temp
    return "vec4", "textureCubeLod(%s, %s, %s)" % (arg1, arg2, arg3)
    
  def function_texture2D(self, params={}):
    temp = params["type"]
    params["type"] = "sampler2D"
    arg1 = self.env.fill_variable_value(params)
    params["type"] = "vec2"
    arg2 = self.env.fill_variable_value(params)
    params["type"] = temp
    if random.randint(1, 2) == 1:
      return "vec4", "texture2D(%s, %s)" % (arg1, arg2)
    else:
      return "vec4", "texture2D(%s, %s, %s)" % (arg1, arg2, self.get_float_value())

  def function_texture2DProj(self, params={}):
    temp = params["type"]
    params["type"] = "sampler2D"
    arg1 = self.env.fill_variable_value(params)
    params["type"] = random.choice(["vec3", "vec4"])
    arg2 = self.env.fill_variable_value(params)
    params["type"] = temp
    if random.randint(1, 2) == 1:
      return "vec4", "texture2DProj(%s, %s)" % (arg1, arg2)
    else:
      return "vec4", "texture2DProj(%s, %s, %s)" % (arg1, arg2, self.get_float_value())

  def function_texture2DProjLod(self, params={}):
    temp = params["type"]
    params["type"] = "sampler2D"
    arg1 = self.env.fill_variable_value(params)
    params["type"] = random.choice(["vec3", "vec4"])
    arg2 = self.env.fill_variable_value(params)
    params["type"] = temp
    return "vec4", "texture2DProjLod(%s, %s, %s)" % (arg1, arg2, self.get_float_value())
      
  def function_texture2DLod(self, params={}):
    temp = params["type"]
    params["type"] = "sampler2D"
    arg1 = self.env.fill_variable_value(params)
    params["type"] = "vec2"
    arg2 = self.env.fill_variable_value(params)
    arg3 = self.get_float_value()
    params["type"] = temp
    return "vec4", "texture2DLod(%s, %s, %s)" % (arg1, arg2, arg3)

  #================================================================================#
  def function_clamp(self, params={}):
    temp = params["type"]
    params["type"] = random.choice([ "float", "vec2", "vec3", "vec4" ])
    rtn_type = params["type"]
    arg1 = self.env.fill_variable_value(params)
    arg2 = self.env.fill_variable_value(params)
    arg3 = self.env.fill_variable_value(params)
    params["type"] = temp
    return rtn_type, "clamp(%s, %s, %s)" % (arg1, arg2, arg3)

  def function_mix(self, params={}):
    temp = params["type"]
    params["type"] = random.choice([ "float", "vec2", "vec3", "vec4" ])
    rtn_type = params["type"]
    arg1 = self.env.fill_variable_value(params)
    arg2 = self.env.fill_variable_value(params)
    arg3 = self.env.fill_variable_value(params)
    params["type"] = temp
    return rtn_type, "mix(%s, %s, %s)" % (arg1, arg2, arg3)
    
  def function_smoothstep(self, params={}):
    temp = params["type"]
    params["type"] = random.choice([ "float", "vec2", "vec3", "vec4" ])
    rtn_type = params["type"]
    arg1 = self.env.fill_variable_value(params)
    arg2 = self.env.fill_variable_value(params)
    arg3 = self.env.fill_variable_value(params)
    params["type"] = temp
    return rtn_type, "smoothstep(%s, %s, %s)" % (arg1, arg2, arg3)

  def function_step(self, params={}):
    temp = params["type"]
    params["type"] = random.choice([ "float", "vec2", "vec3", "vec4" ])
    rtn_type = params["type"]
    arg1 = self.env.fill_variable_value(params)
    arg2 = self.env.fill_variable_value(params)
    params["type"] = temp
    return rtn_type, "step(%s, %s)" % (arg1, arg2)
  ##############################################################