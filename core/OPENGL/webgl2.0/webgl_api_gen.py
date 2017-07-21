import importlib, random, os, sys
sys.path.append(os.path.join(os.getcwd(),"core"))
import util

class GL_API_GEN():
  def __init__(self, moduleNames=None):
    self.api = {}
    if not moduleNames:
      moduleNames = {
        "webgl_buffer"			:  "GL_BUFFER",
        "webgl_frame_buffer"	:  "GL_FRAME_BUFFER",
        "webgl_render_buffer"	:  "GL_RENDER_BUFFER",
        "webgl_depth_buffer"	:  "GL_DEPTH_BUFFER",
        "webgl_texture"			:  "GL_TEXTURE",
        "webgl_culling"			:  "GL_CULLING",
        "webgl_blend"			:  "GL_BLENDING",
        "webgl_stencil"			:  "GL_STENCIL",
        "webgl_type"			:  "GL_TYPE",
        "webgl_canvas"			:  "CanvasRenderingContext2D",
        "webgl_canvas"			:  "WebGLRenderingContext",
      }
    for m_name, c_name in moduleNames.iteritems():
      module = importlib.import_module(m_name)
      obj = getattr(module, c_name)
      my_api = obj.api
      my_api_caller_id = {}
      for api in my_api:
        if "compatibility" in my_api[api]:
          continue
        api_key = "%s--%s" % (c_name,api)
        my_api_caller_id[api_key] = my_api[api]
        if "caller" not in my_api_caller_id[api_key]:
          my_api_caller_id[api_key]["caller"] = obj.caller
        my_api_caller_id[api_key]["api"] = api
      self.api.update(my_api_caller_id)
    
    self.api_weight = {}
    self.weight_api()
    
  def weight_api(self):
    for api in self.api.keys():
      if api not in self.api_weight:
        self.api_weight[api] = 1

  def tag_webgl_api(self, param = {}):
    batch = int(param["batch"]) if "batch" in param else random.randint(50,100)
    scripts = [self.tag_webgl_api_helper(param) for i in range(0, batch)]
    if "try_catch" in param:
      scripts = [ "try { %s } catch(err) {pp(err);}" % s for s in scripts]
    return "\n\t".join(scripts)
    
  def tag_webgl_api_helper(self, param = {}):
    api_key = param["target"] if "target" in param else util.w_choice(self.api_weight)
    cur_api_name = self.api[api_key]["api"]
    if "name_only" in param:
      return cur_api_name
    #print cur_api_name, param
    cur_api_args = self.fill_args(api_key, param)
    if "args_only" in param:
      return cur_api_args
    caller = util.w_choice(self.api[api_key]["caller"])
    if "caller" in param and param["caller"]:
      if len(caller) > 0:
        return "%s.%s(%s)" % (caller, cur_api_name, cur_api_args)
      else:
    	return "%s(%s)" % (cur_api_name, cur_api_args)

    rtn = self.api[api_key]["rtn"]
    if "full" in param and param["full"]:
      if len(caller) > 0:
        if len(rtn)>0:
          return "%s=%s.%s(%s);" % (rtn, caller, cur_api_name, cur_api_args)
        else:
          return "%s.%s(%s);" % (caller, cur_api_name, cur_api_args)
      else:
        if len(rtn)>0:
    	  return "%s=%s(%s);" % (rtn, cur_api_name, cur_api_args)
        else:
          return "%s(%s);" % (cur_api_name, cur_api_args)
    
  def unit_test(self):
    for api_name, api_arg in self.api.iteritems():
      print api_name
      arg = random.choice(api_arg["arg"])
      arg_name = [k.keys()[0] for k in arg]
      print "   %s(%s)" % (api_name, ",".join(arg_name))

  def match_args(self, src_args, targets_args):
     for option in targets_args:
       if option["args"]:
         print ""

  def fill_args(self, fname, argv=None):
    arg = random.choice(self.api[fname]["arg"])
    arg_name = [k.keys()[0] for k in arg]
    return ", ".join(arg_name)

  def get_template_tag(self):
    return {
      "$$[gl_web_api" : {
        "impl" : self.tag_webgl_api,
        "help" : "",
        "i.e." : "",
      }
    }