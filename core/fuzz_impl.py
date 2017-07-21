import random, sys, os, importlib

sys.path.append(os.path.join(os.getcwd(),"core"))
import util
sys.path.append(os.path.join(os.getcwd(), "core", "OPENGL"))
import gl__main
sys.path.append(os.path.join(os.getcwd(), "core", "OPENGL", "webgl2.0"))
import webgl_main, opengl_main

sys.path.append(os.path.join(os.getcwd(), "core", "DOM"))
import dom__main
sys.path.append(os.path.join(os.getcwd(), "core", "DOM", "safari"))
import safari_main

sys.path.append(os.path.join(os.getcwd(), "core", "JS"))
import js__main
sys.path.append(os.path.join(os.getcwd(), "core", "JS", "WebKit"))
import webkit_main

sys.path.append(os.path.join(os.getcwd(), "core", "Heuristic", "jjjj"))
import jjjj_main
#############################################################################
class Fuzz_Runtime:
  def __init__(self, debug=False):
    self.debug = debug
    self.init_block = []
    self.raw_api_info = {}
    self.rtn_api_info = {}
    self.obj_table = {}
    self.grp_info = {}
    self._process_api_info(
      {
        "my_doc"		:{"weight" : 20, "rtn_type" : "DOM_Doc"  },
        "my_win"		:{"weight" : 100, "rtn_type" : "DOM_Win"  },
        "g_canvas"		:{"weight" : 30, "rtn_type" : "HTMLCanvasElement"  },
        "g_context_gl"	:{"weight" : 30, "rtn_type" : "WebGLRenderingContext"},
        "g_context_2d"	:{"weight" : 30, "rtn_type" : "CanvasRenderingContext2D"},
        "callback"		:{"weight" : 30, "rtn_type" : "Callback"},
        "evaluate_rtn"	:{"weight" : 30, "rtn_type" : "XPathResult"},
      }, self.easy_terminator)
    self.simple_init = [
      {"g_DOM_Win"			: {"window":1}},
      {"g_DOM_Doc"			: {"document":1}},
      {"g_DOM_Win_List"		: {"window.frames":1}},
      {"g_Element"			: {"document.createElement('$$[dom_tag_name]')":1}},
      {"g_Canvas_gl"		: {"document.getElementById('webgl_View')":1}},
      {"g_Canvas_2d"		: {"document.getElementById('canvas_View')":1}},
      {"g_ctx_gl"			: {"g_Canvas_gl.getContext('webgl')":1}},
      {"g_ctx_2d"			: {"g_Canvas_2d.getContext('2d')":1}},
    ]
    self.default_name = {
      "g_DOM_Win"			: "DOM_Win",
      "g_DOM_Doc"			: "DOM_Doc",
      "g_DOM_Win_List"		: "DOM_Win_List",
      "g_Element"			: "DOM_Element",
      "g_Canvas_gl"			: "HTMLCanvasElement",
      "g_Canvas_2d"			: "HTMLCanvasElement",
      "g_ctx_gl"			: "WebGLRenderingContext",
      "g_ctx_2d"			: "CanvasRenderingContext2D",
    }
    
  def reset(self):
    self.obj_table = {}
    
  def dump_api_info(self):
    for k, v in self.rtn_api_info.iteritems():
      print k
      print v
      
  def collect_grp_info(self, grp):
    self.grp_info.update(grp)
    
  def select_from_grp(self, grp):
    if grp in self.grp_info:
      return util.w_choice(self.grp_info[grp])
    else:
      return grp

  def init_type_obj(self):
    for init in self.simple_init:
      name = init.keys()[0]
      type = self.default_name[name]
      self._add_to_obj_table(type, name, 5)
      self.init_block.append("try{%s=%s;}catch(err){}" % (name, util.w_choice(init[name])))

  def get_runtime_init(self, param = {}):
    runtime_init_str = []
    for type in self.obj_table:
      if type in self.default_name.values():
        for obj in self.obj_table[type]:
          runtime_init_str.append(
            "%s = %s;" % (
              obj,
              self.default_name.keys()[self.default_name.values().index(type)]))
    return "\n\t".join(runtime_init_str)

  def get_global_var_def(self, param = {}):
    global_var_def_str = []
    for type in self.obj_table:
      for obj in self.obj_table[type]:
        global_var_def_str.append("var %s;" % obj)
    return "\n\t".join(global_var_def_str)

  def interpret_type(self, my_type):
    prev_type = None
    while True:
      prev_type = my_type
      if type(my_type) is list:
        my_type = random.choice(my_type)
      my_type = self.select_from_grp(my_type)
      if my_type == prev_type:
        return my_type

  ###################################################################################
  def easy_terminator(self, param = {}):
    if param['target'] == 'my_doc':
      return "document"
    if param['target'] == 'my_win':
      return "window"
    if param['target'] == 'callback':
      return "$$[JS_Func]"
    if param['target'] == 'evaluate_rtn':
      return "null"
    if param['target'] == 'g_canvas':
      return "g_Canvas"
    if param['target'] == 'g_context_gl':
      return "g_ctx_gl"
    if param['target'] == 'g_context_2d':
      return "g_ctx_2d"
      
  def inline_DOM_Win_gen(self, param = {}):
    pass
  ###################################################################################
      
  def collect_api_info(self, info, api_gen_callback):
    self.raw_api_info.update(info)
    self._process_api_info(info, api_gen_callback)
    
  def _process_api_info(self, info, api_gen):
    for api, data in info.iteritems():
      if "rtn_type" not in data or not data["rtn_type"] or data["rtn_type"] == "void":
        continue
      rtn = data["rtn_type"]
      if rtn not in self.rtn_api_info:
        self.rtn_api_info[rtn] = {}
      self.rtn_api_info[rtn][api] = {
        "weight" : 10 if "weight" not in data else data["weight"],
        "call"   : api_gen,
      }
    #self.dump_api_info()

  ###################################################################################    
  def get_dom_obj(self, param):
    return self.get_js_obj(param)

  def get_js_obj(self, param = {}):
    LR_gen_rate = {
      "l" : { "reuse":random.randint(1, 10), "new":random.randint(1, 5) },
      "r" : { "reuse":random.randint(1, 10), "dyn":random.randint(1, 5) },
    }
    return self._get_obj_help(param, LR_gen_rate)
    
  def get_gl_obj(self, param):
    LR_gen_rate = {
      "l" : { "reuse":random.randint(1, 10), "new":random.randint(1, 5) },
      "r" : { "reuse":random.randint(1, 10), "dyn":random.randint(1, 5) },
    }
    return self._get_obj_help(param, LR_gen_rate)
    
  def add_random_context(self, name, type):
    if name != "window" and \
       random.randint(0, 6) < 2 and \
       type in ["DOM_Win", "DOM_Doc", "DOM_Element", "Node"]:
      return "$$[JS_OBJ??type==DOM_Win&&LorR==r]." + name
    else:
      return name
  ###########################################################################
  def type_confusion_1(self, cur_name, my_type):
    if random.randint(0, 9) < 2:
      new_type = self._get_rand_cls_from_table()
      self._switch_obj_in_table(cur_name, my_type, new_type)
    
  ###########################################################################    
  def _get_obj_help(self, param, LR_gen_rate):
    my_type = self.interpret_type(param["type"]) if "type" in param else "ANY"
    # tluo: Force var convert types
    if random.randint(1, 2) < 2:
      new_name = "%s_%s" % (my_type, random.randint(1, 10))
    else:
      new_name = "shared_%s" % (random.randint(1, 10))
    cur_name = self._get_obj_table(my_type)
    if param['LorR'] == "l":
      new_or_use = util.w_choice(LR_gen_rate["l"])
      if new_or_use == "new" or not cur_name:
        self._add_to_obj_table(my_type, new_name)
        return self.add_random_context(new_name, my_type)
      else:
        self.type_confusion_1(cur_name, my_type)
        return self.add_random_context(cur_name, my_type)

    if param['LorR'] == "r":
      new_or_use = util.w_choice(LR_gen_rate["r"])
      if new_or_use == "reuse":
        if cur_name:
          return self.add_random_context(cur_name, my_type)
        else:
          new_or_use = "dyn"
      if new_or_use == "dyn":
        my_runtime = self._get_runtime_obj(my_type)
        if my_runtime:
          return self.add_random_context(my_runtime, my_type)
      print "[E] No Right Value"
      raise

    print "_get_obj_help:", param, my_type
    print "             :", self.rtn_api_info[my_type]
      
  def _get_runtime_obj(self, type, param={}):
    if type not in self.rtn_api_info:
      print ">>"*10, "NO TYPE Found [%s]" % type
      return None
    my_choice = util.w_choice_1(self.rtn_api_info[type])
    obj = self.rtn_api_info[type][my_choice]["call"]({"target":my_choice, "caller":True, "batch":1})
    return obj
    
  def _add_to_obj_table(self, cls, name, weight=1):
    if cls not in self.obj_table:
      self.obj_table[cls] = {}
    self.obj_table[cls][name] = weight

  def _get_obj_table(self, cls, name=None):
    if cls not in self.obj_table:
      return None
    return util.w_choice(self.obj_table[cls])
    
  def _get_rand_cls_from_table(self):
    random.choice(self.obj_table.keys())
    
  def _switch_obj_in_table(self, name, cls_old, cls_new):
    if cls_old not in self.obj_table or cls_new not in self.obj_table or name not in self.obj_table[cls_old]:
      return False
    self.obj_table[cls_new].append(name)
    self.obj_table[cls_old].remove(name)
    return True
  ###########################################################################
  def get_static_init(self, param={}):
    return "\n\t".join(self.init_block)
    
  def get_template_tag(self):
    return {
      "$$[global_var_init" : {
        "impl" : self.get_global_var_def,
        "help" : "Fuzz_Runtime",
        "i.e." : "",
      },
      "$$[static_init" : {
        "impl" : self.get_static_init,
        "help" : "Fuzz_Runtime",
        "i.e." : "",
      },
      "$$[runtime_init" : {
        "impl" : self.get_runtime_init,
        "help" : "Fuzz_Runtime",
        "i.e." : "",
      },
      "$$[GL_OBJ" : {
        "impl" : self.get_gl_obj,
        "help" : "Fuzz_Runtime",
        "i.e." : "",
      },
      "$$[JS_OBJ" : {
        "impl" : self.get_js_obj,
        "help" : "Fuzz_Runtime",
        "i.e." : "",
      },
      "$$[DOM_OBJ" : {
        "impl" : self.get_dom_obj,
        "help" : "Fuzz_Runtime",
        "i.e." : "",
      },
    }
###########################################################################
class Fuzz_Impl:
  def __init__(self, debug=False):
    self.debug = debug
    self.my_fuzz_tags = Fuzz_Tag()

    my_gl_env = gl__main.GLEnvironment(webgl_main.GL_Web2())
    self.OpenGL_api = my_gl_env.get_gl_api_gen()
    self.OpenGL_type= my_gl_env.get_gl_type()

    self.my_dom_env = dom__main.DOMEnvironment(safari_main.Safari_DOM())
    self.must_have_tag = {
  	  "table":{"needed":1, "spec": [{}]},
  	  "canvas":{"needed":3,
  	     "spec": [
  	       {"att":{"id":"webgl_View"}, "css":{}},
  	       {},
  	       {"att":{"id":"canvas_View"}, "css":{}},
  	     ]
  	  },
	  "iframe":{"needed":1, "spec": [{},{},{},{}]},
	}
    self.DOM_dom_tree = self.my_dom_env.get_dom_tree(must_have_tag=self.must_have_tag)

    my_js_env = js__main.JSEnvironment(webkit_main.JS_WebKit())
    self.JS_api = my_js_env.get_js_api_gen()
    self.JS_prop= my_js_env.get_js_prop_gen()
    self.JS_type= my_js_env.get_js_type()
    
    self.runtime = Fuzz_Runtime(debug=self.debug)
    self.my_fuzz_tags.insert_tag_by_classes({"util":"util"})
    self.my_fuzz_tags.insert_tag_by_instances(self.runtime.get_template_tag())

    self.runtime.collect_api_info(self.OpenGL_api.api, self.OpenGL_api.tag_webgl_api)
    self.runtime.collect_grp_info(self.OpenGL_type.group)
    self.my_fuzz_tags.insert_tag_by_classes(my_gl_env.get_gl_tag())

    self.my_fuzz_tags.insert_tag_by_instances(self.DOM_dom_tree.get_template_tag())
    
    self.runtime.collect_api_info(self.JS_api.api, self.JS_api.tag_js_api)
    self.runtime.collect_api_info(self.JS_prop.prop, self.JS_prop.tag_js_prop)
    self.my_fuzz_tags.insert_tag_by_classes(my_js_env.get_js_fuzz_tags())

    self.my_fuzz_tags.insert_tag_by_classes(self.my_dom_env.get_dom_fuzz_tags())
    
    self.opengl = opengl_main.OpenGL()
    self.my_fuzz_tags.insert_tag_by_instances(self.opengl.get_template_tag())
    
    self.jjjj = jjjj_main.jjjj()
    self.my_fuzz_tags.insert_tag_by_instances(self.jjjj.get_template_tag())
    
    #self.dump_tags()
    self.runtime.init_type_obj()
    
  def reset(self):
    self.DOM_dom_tree.reset()
    self.runtime.reset()
    
  def dump_tags(self):
    ff = open("tag.log", "w")
    for tag, v in self.my_fuzz_tags.tags.iteritems():
      ff.write(tag+"\n")
      #for k, d in v.iteritems():
      #  ff.write(k + "\t"+ str(d)+"\n")
    
  def get_fuzz_tag_names(self):
    return self.my_fuzz_tags.get_fuzz_tag_names()
    
  def fill_tag(self, tag, depth, params):
    my_tag = self.my_fuzz_tags.get_fuzz_tag_objs()
    data = my_tag[tag]["impl"](params)
    if self.debug:
      print "  Get Tag Data:", data
    return data
    
  def unit_test():
    pass
###########################################################################
class Fuzz_Tag:
  def __init__(self, moduleNames=None):
    self.tags = {}
      
  def get_fuzz_tag_objs(self):
    return self.tags
  def get_fuzz_tag_names(self):
    return self.tags.keys()
    
  def _add_to_tags(self, m_name, c_name):
    module = importlib.import_module(m_name)
    obj = getattr(module, c_name)
    self.tags.update(obj().get_template_tag())
      
  def insert_tag_by_instances(self, instances):
    self.tags.update(instances)
    
  def insert_tag_by_classes(self, moduleNames):
    for m_name, c_name in moduleNames.iteritems():
      self._add_to_tags(m_name, c_name)
  