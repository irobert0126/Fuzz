import random, copy

class DOM_Tree():
  # key_tags = {"tag_name":{"needed":#, "att":{}, "css":{}}}
  def __init__(self, cur_env=None, key_tags={}, must_have_tag={}, rules={}):
    self.debug = False
    self.key_tags = key_tags
    self.rules = rules
    self.apply_rule(rules)
    self.must_have_tag = must_have_tag
    self.cur_env = cur_env
    self.css = self.cur_env.get_dom_css()
    
    self.saved_key_tags = copy.deepcopy(self.key_tags)
    self.saved_rules = copy.deepcopy(self.rules)
    self.saved_must_have_tag = copy.deepcopy(self.must_have_tag)
    
    self.must_have_relation_dom = {
      "html" : {"head":1, "body":1},
      "head" : {"title":1, "meta":1},
      "body" : {"div":1, "script":1},
      "table": {"caption":1, "colgroup":1, "thead":1, "tbody":1, "tfoot":1, "tr":3},
      "tr"   : {"th":3, "td":3},
      "colgroup": {"col":3},
    }
    self.only_have_relation_dom = {
    }
    self.only_have_data = {
      "script" : {
        "content":"$$[js_web_api??batch==15&&try_catch==1&&full==1]",
      },
    }

    self.node_count = 1
    self.node_left = 0
    self.meta_info = {}
    self.cur_class_count = 0
    
  def get_template_tag(self):
    return {
      "$$[dom_tree" : {
        "impl" : self.get_dom_tree_html,
        "help" : "dom_tree",
        "i.e." : "$$[dom_tree??max_depth==3&&max_width==3]",
      },
      "$$[dom_tag_name" : {
        "impl" : self.select_dom_tag,
        "help" : "dom_tree",
        "i.e." : "",
      },
      "$$[dom_tag_id" : {
        "impl" : self.get_dom_tag_id,
        "help" : "dom_tree",
        "i.e." : "",
      },
      "$$[dom_class_name" : {
        "impl" : self.dom_class_name,
        "help" : "dom_tree",
        "i.e." : "",
      },
      "$$[dom_class_name_def" : {
        "impl" : self.dom_class_name_def,
        "help" : "dom_tree",
        "i.e." : "",
      },
      "$$[dom_style_def" : {
        "impl" : self.dom_style_def,
        "help" : "dom_tree",
        "i.e." : "",
      },
    }

  #=================================================================================#
  def reset(self):
    self.key_tags = copy.deepcopy(self.saved_key_tags)
    self.rules = copy.deepcopy(self.saved_rules)
    self.must_have_tag = copy.deepcopy(self.saved_must_have_tag)
    self.node_count = 1
    self.cur_class_count = 0
    
  #=================================================================================#
  def dom_class_name_def(self, param = {}):
    self.cur_class_count += 1
    return "class_%s" % self.cur_class_count
    
  def dom_class_name(self, param = {}):
    return "class_%s" % random.randint(0, self.cur_class_count)
    
  def dom_style_def(self, param = {}):
    style_def = []
    for i in range(random.randint(0, 10)):
      style_def.append("$$[css_selector] {%s}" % self.css.get_random_style_css(random.randint(0, 10)))
    return "\n\t".join(style_def)
  #=================================================================================#
  def apply_rule(self, rules):
    if "no_tag" in rules:
      for tag in rules["no_tag"]:
        if tag in DOM_Elements:
          DOM_Elements.remove(tag)

  def update_tags(self, set, tag):
    if not set or not tag:
      return None
    if tag in set:
      if set[tag]["needed"] > 1:
        set[tag]["needed"] -= 1
      else:
        set.pop(tag, None)

  def select_dom_tag(self, param={}):
    return self.cur_env.get_dom_tag()
    
  def _get_random_tag(self, cur_node, context=None):
    if len(self.must_have_tag) > 0:
      r = random.randrange(0, self.node_left) if self.node_left > 0 else 0
      if r == 0:
        tag = random.choice(self.must_have_tag.keys())
        meta = self.must_have_tag[tag]["spec"][self.must_have_tag[tag]["needed"]-1]
        self.update_tags(self.must_have_tag, tag)
        return tag, meta

    if not context:
      return self.cur_env.get_dom_tag(), None
      
    if "width" in context and "depth" in context:
      probability = context["width"]*context["depth"]
      r = random.randrange(0, probability)
      if len(self.key_tags) > 0 and r < (probability/len(self.key_tags)):
        tag = random.choice(self.key_tags.keys())
        meta = self.key_tags[tag]
        self.update_tags(self.key_tags, tag)
        return tag, None
      else:
        return self.cur_env.get_dom_tag(), None

  def _get_only_have_children(self, cur_tag):
    tags = []
    if cur_tag not in self.only_have_relation_dom:
      return None
    only_have = self.only_have_relation_dom[cur_tag]
    for key in only_have:
      tags.extend([key]*only_have[key])
    return tags

  def _get_must_have_children(self, cur_tag):
    tags = []
    if cur_tag not in self.must_have_relation_dom:
      return tags
    must_have = self.must_have_relation_dom[cur_tag]
    for key in must_have:
      tags.extend([key]*must_have[key])
    return tags

  def create_a_node(self, tag, meta=None):
    cur_node = self.cur_env.get_dom_node(tag, attr={}, css={"position":1})
    if meta and "att" in meta and "id" in meta["att"]:
      cur_node.id = meta["att"]["id"]
    else:
      cur_node.id = "DOM_id_"+str(self.node_count)
    self.node_count += 1
    
    cur_node.body_before = "[B:%s]" % tag
    cur_node.body_after = "[A:%s]" % tag
    if meta:
      if "att" in meta:
        cur_node.pre_define_attr(meta["att"])
      if "css" in meta:
        cur_node.pre_define_css(meta["css"])
    cur_node.get_must_have_attrib(tag)
    return cur_node
    
  ###################################################################################
  def get_dom_tree_html(self, param = {}):
    return self.construct_dom_tree(param).serialize()
    
  def construct_dom_tree(self, param = {}):
    root_tag="html" if "root" not in param else param["root"]
    max_depth =random.randint(1, 6) if "max_depth" not in param else int(param["max_depth"])
    breadth   =random.randint(1, 4) if "max_width" not in param else int(param["max_width"])
    self.node_left = pow(breadth, max_depth)
    root_node = self.create_a_node(root_tag)
    self.construct_dom_tree_DFS(root_node, 0, max_depth, breadth)
    #self.meta_info = root_node.collect_info()
    return root_node

  def construct_dom_tree_DFS(self, prev_node, cur_depth, max_depth, breadth):
    if cur_depth >= max_depth:
      return False
    if prev_node.tag in self.only_have_data:
      prev_node.body_before = self.only_have_data[prev_node.tag]["content"]
      prev_node.body_after = self.only_have_data[prev_node.tag]["content"]
      return True
      
    only_have_children = self._get_only_have_children(prev_node.tag)
    if only_have_children:
      for child in only_have_children:
        child_node = self.create_a_node(child)
        self.construct_dom_tree_DFS(child_node, cur_depth, max_depth, breadth)
        prev_node.add_child(child_node)
      return True
        
    must_have_children = self._get_must_have_children(prev_node.tag)
    for child in must_have_children:
      child_node = self.create_a_node(child)
      self.construct_dom_tree_DFS(child_node, cur_depth, max_depth, breadth)
      prev_node.add_child(child_node)

    for i in range(0, breadth-len(must_have_children)):
      rand_tag, meta = self._get_random_tag(prev_node, {"width":breadth, "depth":max_depth})
      #while rand_tag in must_have_children:
      #  rand_tag, meta = self._get_random_tag(prev_node, {"width":breadth, "depth":max_depth})
      child_node = self.create_a_node(rand_tag, meta)
      self.construct_dom_tree_DFS(child_node, cur_depth+1, max_depth, breadth)
      self.node_left -= 1
      prev_node.add_child(child_node)
    return True

  #==============================================================#

  def get_dom_tag_id(self, param={}):
    return "DOM_id_%s" % random.randint(1, self.node_count)

  def dom_tree_unit_test(self):
    print "\n[+] DOM TREE GEN Test:"
    dom = self.construct_dom_tree()
    page = dom.serialize()
    print page[:500]
    
if __name__ == "__main__":
  dom_gen = DOM_Generator(
        {"table":{"needed":1}},
        {"canvas":{"needed":1, "att":{"id":"webglView"}, "css":{}}},
        {"iframe":{"needed":1}},
  )
  dom = dom_gen.construct_dom_tree()
  page = dom.serialize()
  print dom_gen.get_random_tag()