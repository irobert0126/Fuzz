import random

qualifier_to_type_map = {
   "attribute" :["float", "vec2", "vec3", "vec4", "mat2", "mat3", "mat4"],
   "uniform"   :["float", "vec2", "vec3", "vec4", "mat2", "mat3", "mat4", "sampler2D", "samplerCube"],
   "varying"   :["float", "vec2", "vec3", "vec4", "mat2", "mat3", "mat4"],
   "local"     :["float", "vec2", "vec3", "vec4", "mat2", "mat3", "mat4"],
}    
# make sure we declare a varying variable of the same type and name 
# in both the vertex shader and the fragment shader.
env_state_var_map = {
   "vertex" 	: ["uniform", "attribute", "varying", "local"],
   "fragment"	: ["uniform", "varying", "local"],
} 
precision = ["highp", "mediump", "lowp"]

built_in_var = {
  "vertex"   : {"gl_Position" : "vec4", "gl_PointSize": "float"},
  "fragment" : {"gl_FragColor": "vec4", "gl_FragData[0]": "vec4", "gl_FragData[1]": "vec4", 
                "gl_FragData[2]": "vec4", "gl_FragData[3]": "vec4"}
}

class opengl_var():
  def __init__(self, env):
    self.env = env
  
  #============================================================================#
  def get_rand_param(self):
    param = {}
    param["state"] = random.choice(["vertex", "fragment"])
    param["qualifier"] = self.get_rand_qualifier_by_state(param["state"])
    param["type"] = self.get_rand_type_by_qualifier(param["qualifier"])
    param["lorr"] = random.choice(["left", "right"])
    param["id"] = -1
    return param
    
  # ["vertex", "fragment"] to [qualifier]
  @staticmethod
  def get_rand_qualifier_by_state(state):
    return random.choice(env_state_var_map[state])
    
  # ["attribute", "uniform", "varying", "local"] to [type]
  @staticmethod
  def get_rand_type_by_qualifier(qualifier):
    return random.choice(qualifier_to_type_map[qualifier])
    
  @staticmethod
  def create_var_name(param = None, type = None, qualifier = None):
    if not param:
      raise Exception('OpenGL var', 'create_var_name without info')
    return "%s_%s_%s" % (qualifier if qualifier else param["qualifier"], type if type else param["type"], param["id"])
  #======================= attribute ======================================#
  @staticmethod
  def gen_attribute_decl(self, param = {}):
    type = opengl_var.get_rand_type_by_qualifier("attribute")
    precision = random.choice(precision) if "precision" not in param else param["precision"]
    id = random.randint(1, 100) if "id" not in param else param["id"]
    return "attribute %s %s attribute_%s_%s;\n" % (precision, type, type, id)
  #============================ varying ========================================#
  @staticmethod
  def gen_varying_decl(self):
    type = opengl_var.get_rand_type_by_qualifier("varying")
    precision = random.choice(precision) if "precision" not in param else param["precision"]
    id = random.randint(1, 100) if "id" not in param else param["id"]
    return "varying %s %s varying_%s_%s;\n" % (precision, type, type, id)
  #============================ uniform ========================================#
  @staticmethod
  def gen_uniform_decl(self, state=""):
    type = opengl_var.get_rand_type_by_qualifier("uniform")
    precision = random.choice(precision) if "precision" not in param else param["precision"]
    id = random.randint(1, 100) if "id" not in param else param["id"]
    return "uniform %s %s uniform_%s_%s;\n" % (precision, type, type, id)
  #============================ local ========================================#
  @staticmethod
  def gen_local_decl(self, state=""):
    type = opengl_var.get_rand_type_by_qualifier("local")
    prec = random.choice(precision) if "precision" not in param else param["precision"]
    id = random.randint(1, 100) if "id" not in param else param["id"]
    return "%s %s local_%s_%s;\n" % (prec, type, type, id)    
  #$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$#$%#$%#$%#$%#$%
  @staticmethod
  def gen_decl(params, name):
    prec = random.choice(precision) if "precision" not in params else params["precision"]
    qualifier = "" if params["qualifier"] == "local" else params["qualifier"]
    return "%s %s %s %s;" % (qualifier, prec, params["type"], name)    

