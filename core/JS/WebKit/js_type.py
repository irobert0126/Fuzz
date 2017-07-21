import random, math, os, sys

sys.path.append(os.path.join(os.getcwd(), "core"))
import util

# Maintain all the existing JavaScript objects.
# For retrieve a JavaScript object with given type.

class JS_TYPE:
  api = {
  }
  group = {
    "Node": {
      "DOM_Element":1,
      "Attr":1,
      #"Text":1,
      #"Comments":1,
      "DOM_Doc":1,
    }
  }
  def __init__(self):
    pass
    
  def dummy_impl(self, param = {}):
    if param["tag"] == "$$[url_new_window]":
      return "simple.html"
    if param["tag"] == "$$[dom_attr_name]":
      return "id"
    if param["tag"] == "$$[dom_name_name]":
      return "my_html_tag_name"
      
    if param["tag"] == "$$[color]":
      return "red"
    if param["tag"] == "$$[pseudo-elements]":
      return "null"
    if param["tag"] == "$$[namespace]":
      return "http://help.dottoro.com/NS"
    if param["tag"] == "$$[expression_str]":
      return "//*[@id=\"content\"]/div[3]/ul/li[1]/strong"
    if param["tag"] == "$$[namespaceURLMapper]":
      return "null"
    if param["tag"] == "$$[WindowFeaturesStr]":
      return "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes"
    # https://developer.mozilla.org/en-US/docs/Web/API/Window/showModalDialog
    if param["tag"] == "$$[showModalDialog_options]":
      return "null"
    if param["tag"] == "$$[showModalDialog_arguments]":
      return "null"
    if param["tag"] == "$$[Rand_Html]":
      return "<html><body></html>"
    if param["tag"] == "$$[win-mediaQuery-string]":
      return "(min-width: 400px)"
      
  # For Unimplemented Tags
  def get_template_tag(self):
    return {
      "$$[url_new_window" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[dom_attr_name" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[dom_name_name" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[Rand_Html" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[pseudo-elements" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[namespace" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[expression_str" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[namespaceURLMapper" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[WindowFeaturesStr" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[showModalDialog_arguments" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[showModalDialog_options" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
      "$$[win-mediaQuery-string" : {
        "impl" : self.dummy_impl,
        "help" : "unimplemented",
        "i.e." : "",
      },
    }