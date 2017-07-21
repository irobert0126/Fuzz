import sys, os
import dom_attr, dom_css, dom_node
#-----------------------------------------------------------------------#
# The Abstract Factory:
class DOMFactory:
    def make_dom_tag(self):   pass
    def make_dom_attri(self): pass
    def make_dom_css(self):   pass
    def make_dom_node(self):  pass
    def make_dom_tree(self):  pass

# Anyone who wants to access DOM APIs
# should ONLY use this file. 
# Other details should not be exposed.
class DOMEnvironment():
  def __init__(self, factory):
    self.factory = factory
    
  def get_dom_fuzz_tags(self):
    return self.factory.make_dom_fuzz_tags()

  def get_dom_tag(self):
    return self.factory.make_dom_tag()
  
  def get_dom_attr(self, spec_attr={}):
    attr = self.factory.make_dom_attr()
    if spec_attr is not None:
      attr.select_attrib(spec_attr=spec_attr)
    return attr

  def get_dom_css(self, spec_css={}):
    css = self.factory.make_dom_css()
    if spec_css is not None:
      css.select_css(spec_css=spec_css)
    return css

  def get_dom_node(self, tag=None, attr={}, css={}, event={}):
    node = self.factory.make_dom_node(tag)
    node.attrib = self.get_dom_attr(attr)
    node.css    = self.get_dom_css(css)
    node.event  = event
    return node

  def get_dom_tree(self, key_tags={}, must_have_tag={}, rules={}):
    tree = self.factory.make_dom_tree(self, key_tags, must_have_tag, rules)
    return tree
#-----------------------------------------------------------------------#

def factory_unit_test(environment):
  environment.get_dom_attr().dom_attr_unit_test()
  environment.get_dom_css().dom_css_unit_test()
  environment.get_dom_node().dom_node_unit_test()
  environment.get_dom_tree(  
        must_have_tag={{"table":{"needed":1}},
        {"canvas":{"needed":1, "att":{"id":"webglView"}, "css":{}}},
        {"iframe":{"needed":4}}}
  ).dom_tree_unit_test()
  
###########################################################################
if __name__ == "__main__":
  sys.path.append(os.path.join(os.getcwd(), "core", "DOM", "safari"))
  safari_main = importlib.import_module("safari_main")
  my_env = DOMEnvironment(safari_main.Safari_DOM())
  factory_unit_test(my_env)

