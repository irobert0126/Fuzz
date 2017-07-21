import os, sys, random

sys.path.append(os.path.join(os.getcwd(),"core"))
import util

# Static QUERY DOM Node
class DOM_Walker:
  tree_walker_whatToShow = {
    "NodeFilter.SHOW_ALL":100,
    "NodeFilter.SHOW_ATTRIBUTE":2,
    "NodeFilter.SHOW_CDATA_SECTION":2,
    "NodeFilter.SHOW_COMMENT":2,
    "NodeFilter.SHOW_DOCUMENT":2,
    "NodeFilter.SHOW_DOCUMENT_FRAGMENT":2,
    "NodeFilter.SHOW_DOCUMENT_TYPE":2,
    "NodeFilter.SHOW_ELEMENT":100,
    "NodeFilter.SHOW_ENTITY":2,
    "NodeFilter.SHOW_ENTITY_REFERENCE":2,
    "NodeFilter.SHOW_NOTATION":2,
    "NodeFilter.SHOW_PROCESSING_INSTRUCTION":2,
    "NodeFilter.SHOW_TEXT":20,
  }
  tree_walker_filter = {
    "NodeFilter.FILTER_ACCEPT":100,
    "NodeFilter.FILTER_REJECT":50,
    "NodeFilter.FILTER_SKIP":50
  }
  def __init__(self):
    pass
    
  def select_tree_walker_whatToShow(self, params= {}):
    events = [util.w_choice(DOM_Walker.tree_walker_whatToShow) for i in range(random.randint(1,len(DOM_Walker.tree_walker_whatToShow)-1))]
    return "|".join(events)
    
  #TODO: https://developer.mozilla.org/en-US/docs/Web/API/Document/createNodeIterator#Example
  def select_tree_walker_filter(self, params= {}):
    return "function (node){ return NodeFilter.FILTER_ACCEPT;}"
    
  def get_template_tag(self):
    return {
      "$$[dom_iter_NodeFilter_whatToShow" : {
        "impl" : self.select_tree_walker_whatToShow,
        "help" : "dom_walker",
        "i.e." : "",
      },
      "$$[dom_iter_NodeFilter_filter" : {
        "impl" : self.select_tree_walker_filter,
        "help" : "dom_walker",
        "i.e." : "",
      },
    }