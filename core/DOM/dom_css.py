import random

class CSS:
  def __init__(self, DOM_CSS = None):
    self.css_pool = DOM_CSS
    self.selected_css = {}
  
  def _get_random_css_name(self, tag=""):
    return random.choice(self.css_pool.keys())

  def _get_random_css_value(self, css, tag=""):
    value = random.choice(self.css_pool[css].keys())
    return value

  def insert_css(self, name, value):
    self.selected_css[name] = value
    
  def fill_css(self, css):
    if css in self.css_pool:
      self.selected_css[css] = self._get_random_css_value(css)

  def select_css(self, num=10, tag="", allow_dup=False, spec_css={}):
    i = 0
    while i < num:
      name = self._get_random_css_name(tag)
      if not allow_dup and name in self.selected_css:
        continue
      i += 1
      self.selected_css[name] = self._get_random_css_value(name)
    for kSpec in spec_css:
      vSpec = spec_css[kSpec]
      if isinstance(vSpec, str):
        self.selected_css[kSpec] = vSpec
      elif (random.random() < vSpec):
        self.selected_css[kSpec] = self._get_random_css_value(kSpec)

  def select_a_css(self, meta={}):
    css = meta["key"] if "key" in meta else self._get_random_css_name()
    value= meta["value"] if "value" in meta else self._get_random_css_value(css)
    return css, value

  def serialize(self, attrib_js=False):
    str = "style=\""
    for css in self.selected_css:
      str += "%s:%s; " % (css, self.selected_css[css])
    return str+"\""
    
  def get_random_style_css(self, num):
    self.selected_css = {}
    self.select_css(num)
    return " ".join(["%s:%s; " % (css, self.selected_css[css]) for css in self.selected_css])
    
  def dom_css_unit_test(self):
    print "\n[+] DOM CSS Test"
    print "--- Select random 10 css:"
    self.select_css()
    print self.serialize()
    
if __name__ == "__main__":
  css = CSS()
  css.select_css()
  print css.serialize()