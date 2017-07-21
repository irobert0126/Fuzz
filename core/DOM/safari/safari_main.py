import os, sys, random
import dom_conf

sys.path.append(os.path.join(os.getcwd(), ".."))
import dom__main, dom_attr, dom_css, dom_node, dom_tree

#-----------------------------------------------------------------------#
# Concrete factories:
class Safari_DOM(dom__main.DOMFactory):
  def make_dom_tag(self):
     return random.choice(dom_conf.load_dom_tags())
     
  def make_dom_attr(self):
    return dom_attr.Attribute(dom_conf.load_dom_attr(), dom_conf.load_must_have_attr())
    
  def make_dom_css(self):
    return dom_css.CSS(dom_conf.load_dom_css())
    
  def make_dom_node(self, tag=None, attr=None, css=None, event=None):
    return dom_node.Node(tag = tag if tag else random.choice(dom_conf.load_dom_tags()))
    
  def make_dom_tree(self, cur_env, key_tags, must_have_tag, rules):
    return dom_tree.DOM_Tree(cur_env, key_tags, must_have_tag, rules)
    
  def make_dom_fuzz_tags(self):
    return {
      "dom_selector"	: "DOM_Selector",
      "dom_walker"		: "DOM_Walker",
    }
#-----------------------------------------------------------------------#

  