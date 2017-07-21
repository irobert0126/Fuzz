import os, sys, random

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

# Static QUERY DOM Node
class DOM_Selector:
  # TODO: Selector Rules
  # https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_Started/Selectors
  dom_selecto = {
      "*":5,
      "$$[dom_tag_name??spec==exist]"                                 :55,
      ".$$[dom_class_name]"                                           :50,
      "#$$[dom_tag_id]"                                               :55,
      "$$[dom_tag_name??spec==exist].$$[dom_class_name]"              :50,
      "$$[dom_tag_name??spec==exist]#$$[dom_tag_id]"                  :10,
      #"$$[dom_tag_name??spec==exist][$$[DOM_Attr]]"                  :1,
      "$$[dom_tag_name??spec==exist] > $$[dom_tag_name??spec==exist]" :5,
      "$$[dom_tag_name??spec==exist] $$[dom_tag_name??spec==exist]"   :5,
      "$$[dom_tag_name??spec==exist] + $$[dom_tag_name??spec==exist]" :5,
      "$$[dom_tag_name??spec==exist] ~ $$[dom_tag_name??spec==exist]" :5,
      #"'$$[dom_tag_name][title$=\"hello\"]",
      #"'$$[dom_tag_name][title^=\"hello\"]",
      #"'$$[dom_tag_name][title|=\"hello\"]",
      #"'$$[dom_tag_name][title~=\"hello\"]",
  }
  css_selector = {
    "$$[dom_tag_name]"   						: 10,
    "#$$[dom_tag_id]"    						: 10,
    ".$$[dom_class_name_def]" 					: 10,
    "$$[dom_tag_name].$$[dom_class_name_def]"   : 10,
  }
    
  def select_dom_selector(self, param = {}):
    return util.w_choice(DOM_Selector.dom_selecto)
  def select_css_selector(self, param = {}):
    return util.w_choice(DOM_Selector.css_selector)
    
  def get_template_tag(self):
    return {
      "$$[dom_selectors" : {
        "impl" : self.select_dom_selector,
        "help" : "dom_selector",
        "i.e." : "",
      },
      "$$[css_selector" : {
        "impl" : self.select_css_selector,
        "help" : "dom_selector",
        "i.e." : "",
      },
    }