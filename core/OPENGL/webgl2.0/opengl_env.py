import random, copy
import opengl_var

# Save All of the variable runtime information
class env:
  def __init__(self):
    self.env_var_init = {
      "const"	  : {}, 
      "attribute" : {"float":[], "vec2":[], "vec3":[], "vec4":[], "mat2":[], "mat3":[], "mat4":[]},
      "uniform"   : {"float":[], "vec2":[], "vec3":[], "vec4":[], "mat2":[], "mat3":[], "mat4":[], "sampler2D":[], "samplerCube":[]},
      "local"     : {"float":[], "vec2":[], "vec3":[], "vec4":[], "mat2":[], "mat3":[], "mat4":[]},
    }
    self.env_var = {
      "vertex"   : copy.deepcopy(self.env_var_init),
      "fragment" : copy.deepcopy(self.env_var_init),
      "shared"	 : {
         "varying"   : {"float":[], "vec2":[], "vec3":[], "vec4":[], "mat2":[], "mat3":[], "mat4":[]}
      }
    }
    self.reuse_rate = {"left":30, "right":30}
    self.recursive_rate = 30
    
  #===================   add/reuse variable  =====================================#
  def reuse_dice(self, param = {}):
    lr = param["lorr"]
    if random.randint(0, 100) < self.reuse_rate[lr]:
      return True
    else:
      return False
    
  def pick_variable(self, param = {}):
    if "state" not in param:
      raise Exception('OpenGL', 'pick variable without state info')
      
    state = param["state"]
    param["qualifier"] = opengl_var.opengl_var.get_rand_qualifier_by_state(state) if "qualifier" not in param else param["qualifier"]
    param["type"] = opengl_var.opengl_var.get_rand_type_by_qualifier(qualifier) if "type" not in param else param["type"]
    reuse = self.reuse_dice(param)
    if reuse:
      return self.reuse_vars(param)
    else:
      return self.gen_new_vars(param)
      
  def reuse_vars(self,  param = {}):
    candidate_set = self.get_var_candidate(param)
    if len(candidate_set) == 0:
      my_var = self.gen_new_vars(param)
      return my_var
    return random.choice(candidate_set)
    
  def gen_new_vars(self,  param = {}, spec_type=None, spec_qualifier=None):
    if "qualifier" not in param:
      param["qualifier"] = opengl_var.opengl_var.get_rand_qualifier_by_state(param["state"])
    candidate_set = self.get_var_candidate(param, spec_type)
    param["id"] = len(candidate_set)
    my_var = opengl_var.opengl_var.create_var_name(param, spec_type)
    candidate_set.append(my_var)
    print my_var, spec_type, param
    return my_var

  def get_var_candidate(self, param, spec_type=None):
    type = spec_type if spec_type else param["type"]
    if type in ["sampler2D", "samplerCube"]:
      return self.env_var[param["state"]]["uniform"][type]      
    if param["qualifier"] == "varying":
      return self.env_var["shared"]["varying"][type]
    else:
      return self.env_var[param["state"]][param["qualifier"]][type]
    
  #$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$#$%#$%#$%$
  def dump_declaration(self, params={}):
    declaration = ""
    cur_params = {}
    cur_params["state"] = params["state"]
    state = self.env_var[cur_params["state"]]
    for qualifier in state:
      cur_params["qualifier"] = qualifier
      for type in state[qualifier]:
        cur_params["type"] = type
        declaration += "\n".join([opengl_var.opengl_var.gen_decl(cur_params, name) for name in state[qualifier][type]]) + "\n"
    return declaration
        
  def dump_shared(self):
    declaration = ""
    cur_params = {}
    cur_params["state"] = "shared"
    cur_params["qualifier"] = "varying"
    qualifier = self.env_var[cur_params["state"]][cur_params["qualifier"]]
    for type in qualifier:
      cur_params["type"] = type
      declaration += "\t\t\n".join([opengl_var.opengl_var.gen_decl(cur_params, name) for name in qualifier[type]]) + "\n"
    return declaration

  def fill_build_in(self, params):
     built_in_var = opengl_var.built_in_var[params["state"]]
     rtn = ""
     for var in built_in_var:
       rtn += "%s = %s;\n" % (var, self.fill_variable_value({"state":params["state"], "type":built_in_var[var]}))
     return rtn
  #=================== generate new variable =====================================#           
  def fill_variable_value(self, params):
    cur_depth = 0
    if params["type"] == "float":
      return self.fill_float(params);
    if params["type"] == "vec2":
      return self.fill_vec2(params);
    if params["type"] == "vec3":
      return self.fill_vec3(params);
    if params["type"] == "vec4":
      return self.fill_vec4(params);
    if params["type"] == "mat2":
      return self.fill_mat2(params);
    if params["type"] == "mat3":
      return self.fill_mat3(params);
    if params["type"] == "mat4":
      return self.fill_mat4(params);
    if params["type"] == "sampler2D":
      return self.fill_sampler2D(params);
    if params["type"] == "samplerCube":
      return self.fill_samplerCube(params);
    return "Not-Impl%s" % type[2:]
    
  def get_float_value(self):
    return "%s%s.%s" % (random.choice([" -",""]), random.randint(0, 100000), random.randint(0, 1000))
    
  def fill_float(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      return "%s%s.%s" % (random.choice([" -",""]), random.randint(0, 100000), random.randint(0, 1000))
    value = self.gen_new_vars(param, "float")
    return value
  
  def fill_vec2(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      choice = random.randint(1, 2)
    else:
      choice = random.randint(1, 10)
    if choice == 1:
      return self.gen_new_vars(param, "vec2")     
    if choice == 2:
      return "vec2(%s, %s)" % (self.fill_float(param), self.fill_float(param)) 
    if choice == 3:
      return "(%s)[%s]" % (self.fill_mat2(param), random.randint(0, 1)) 
    if choice == 4:
      return "(%s).%s" % (self.fill_vec4(param), random.choice(["xy","xz","xw","yz","yw","zw"])) 
    if choice == 5:
      return "(%s).%s" % (self.fill_vec3(param), random.choice(["xy","xz","yz"])) 
    if choice == 6:
      return "%s%s(%s)" % (self.fill_float(param), random.choice(["*","+"]), self.fill_vec2(param)) 
    if choice == 7:
      return "(%s)%s%s" % (self.fill_vec2(param), random.choice(["-", "/"]), self.fill_float(param)) 
    if choice == 8:
      return "(%s)%s(%s)" % (self.fill_mat2(param), "*", self.fill_vec2(param))
    if choice == 9:
      return "(%s)%s(%s)" % (self.fill_vec2(param), "+", self.fill_vec2(param)) 
    if choice == 10:
      return "(%s)%s(%s)" % (self.fill_vec2(param), "*", self.fill_mat2(param))
            
  def fill_vec3(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      choice = random.randint(1, 2)
    else:
      choice = random.randint(1, 11)
    if choice == 1:
      return self.gen_new_vars(param, "vec3")     
    if choice == 2:
      return "vec3(%s, %s, %s)" % (self.fill_float(param), self.fill_float(param), self.fill_float(param))
    if choice == 3:
      return "vec3(%s, %s)" % (self.fill_vec2(param), self.fill_float(param))
    if choice == 4:
      return "vec3(%s, %s)" % (self.fill_float(param), self.fill_vec2(param))
    if choice == 5:
      return "(%s)[%s]" % (self.fill_mat3(param), random.randint(0, 2)) 
    if choice == 6:
      return "(%s).%s" % (self.fill_vec4(param), random.choice(["xyz","xyw","xzw","yzw"])) 
    if choice == 7:
      return "(%s).%s" % (self.fill_vec3(param), random.choice(["xy","xz","yz"])) 
    if choice == 8:
      return "%s%s(%s)" % (self.fill_float(param), random.choice(["*","+"]), self.fill_vec3(param)) 
    if choice == 9:
      return "(%s)%s%s" % (self.fill_vec3(param), random.choice([" - ", "/"]), self.fill_float(param)) 
    if choice == 10:
      return "(%s)%s(%s)" % (self.fill_mat3(param), "*", self.fill_vec3(param))
    if choice == 11:
      return "(%s)%s(%s)" % (self.fill_vec3(param), "+", self.fill_vec3(param)) 
    if choice == 12:
      return "(%s)%s(%s)" % (self.fill_vec3(param), "*", self.fill_mat3(param))

  def fill_vec4(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      choice = random.randint(1, 2)
    else:
      choice = random.randint(1, 10)
    if choice == 1:
      return self.gen_new_vars(param, "vec4")     
    if choice == 2:
      return "vec4(%s, %s, %s, %s)" % (self.fill_float(param), self.fill_float(param), self.fill_float(param), self.fill_float(param))
    if choice == 3:
      return "vec4(%s, %s)" % (self.fill_vec3(param), self.fill_float(param))
    if choice == 4:
      return "vec4(%s, %s)" % (self.fill_float(param), self.fill_vec3(param))
    if choice == 5:
      return "vec4(%s, %s)" % (self.fill_vec2(param), self.fill_vec2(param))
    if choice == 6:
      return "(%s)[%s]" % (self.fill_mat4(param), random.randint(0, 3))
    if choice == 6:
      return "(%s)%s(%s)" % (self.fill_mat4(param), "*", self.fill_vec4(param))
    if choice == 7:
      return "(%s)%s(%s)" % (self.fill_vec4(param), "+", self.fill_vec4(param)) 
    if choice == 8:
      return "(%s)%s(%s)" % (self.fill_vec4(param), "*", self.fill_mat4(param))
    if choice == 9:
      return "(%s)%s%s" % (self.fill_vec4(param), random.choice([" - ", "/"]), self.fill_float(param)) 
    if choice == 10:
      return "%s%s(%s)" % (self.fill_float(param), random.choice(["*","+"]), self.fill_vec4(param))

  #------------------------------------------------------------------------------#
  def fill_mat2(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      choice = random.randint(1, 2)
    else:
      choice = random.randint(1, 4)
    if choice == 1:
      return self.gen_new_vars(param, "mat2")     
    if choice == 2:
      return "mat2(%s, %s, %s, %s)" % (self.fill_float(param), self.fill_float(param), self.fill_float(param), self.fill_float(param))
    if choice == 3:
      return "mat2(%s, %s)" % (self.fill_vec2(param), self.fill_vec2(param))
    if choice == 4:
      return "mat2(%s * %s)" % (self.fill_mat2(param), self.fill_mat2(param))

  def fill_mat3(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      choice = random.randint(1, 2)
    else:
      choice = random.randint(1, 4)
    if choice == 1:
      return self.gen_new_vars(param, "mat3")
    if choice == 2:
      value = [self.get_float_value() for p in range(0, 9)]
      return "mat3(%s)" % (",".join(value))
    if choice == 3:
      return "mat3(%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (
       self.fill_float(param), self.fill_float(param), self.fill_float(param),
       self.fill_float(param), self.fill_float(param), self.fill_float(param),
       self.fill_float(param), self.fill_float(param), self.fill_float(param))
    if choice == 4:
      return "mat3(%s, %s, %s)" % (self.fill_vec3(param), self.fill_vec3(param), self.fill_vec3(param))

  def fill_mat4(self, param):
    choice = random.randint(1, 100)
    if choice > self.recursive_rate:
      choice = random.randint(1, 2)
    else:
      choice = random.randint(1, 3)
    if choice == 1:
      return self.gen_new_vars(param, "mat4")
    if choice == 2:
      value = [self.get_float_value() for p in range(0, 16)]
      return "mat4(%s)" % (",".join(value))
    if choice == 3:
      return "mat4(%s, %s, %s, %s)" % (self.fill_vec4(param), self.fill_vec4(param), self.fill_vec4(param), self.fill_vec4(param))

  def fill_sampler2D(self, param):
    return self.gen_new_vars(param, "sampler2D")    

  def fill_samplerCube(self, param):
    return self.gen_new_vars(param, "samplerCube")   
