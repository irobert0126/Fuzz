import random

class Attribute():
  def __init__(self, DOM_Attrib_All=None, DOM_Must_Have_Attrib=None):
    self.debug = False
    self.attribute_pool = DOM_Attrib_All
    self.DOM_Must_Have_Attrib = DOM_Must_Have_Attrib
    self.selected_attrib = {}
    
  #############################################################
  def _get_random_attrib_name(self, tag=""):
    return random.choice(self.attribute_pool.keys())

  def _get_random_attrib_value(self, attrib, tag=""):
    value = random.choice(self.attribute_pool[attrib].keys())
    return value

  def insert_attrib(self, name, value):
    self.selected_attrib[name] = value
    
  def fill_attrib(self, attr):
    if attr in self.attribute_pool:
      self.selected_attrib[attr] = self._get_random_attrib_value(attr)

  def select_a_attrib(self, meta={}):
    attr = meta["key"] if "key" in meta else self._get_random_attrib_name()
    value= meta["value"] if "value" in meta else self._get_random_attrib_value(attr)
    return attr, value

  #############################################################
  def select_attrib(self, max_num=10, allow_dup=False, spec_attr={}):
    cur_num = 0
    while cur_num < max_num:
      name = random.choice(self.attribute_pool.keys())
      if not allow_dup and name in self.selected_attrib:
        continue
      cur_num = cur_num + 1
      self.selected_attrib[name] = self._get_random_attrib_value(name)

    for kSpec in spec_attr:
      vSpec = spec_attr[kSpec]
      if isinstance(vSpec, str):
        self.selected_attrib[kSpec] = vSpec
      elif (random.random() < vSpec):
        self.selected_attrib[kSpec] = self._get_random_attrib_value(kSpec)

  def fill_must_have_attrib(self, tag):
    if tag not in self.DOM_Must_Have_Attrib:
      return None
    mh_attrib = self.DOM_Must_Have_Attrib[tag]
    for k, v in mh_attrib.iteritems():
      self.selected_attrib[k] = random.choice(v.keys())

  #############################################################
  def serialize(self, attrib_js=False):
    str = ""
    for attrib in self.selected_attrib:
      str += "%s='%s' " % (attrib, self.selected_attrib[attrib])
    return str

  def dom_attr_unit_test(self):
    print "\n[+] DOM Attribute Test"
    print "--- Select random 10 attributes:"
    self.select_attrib()
    print self.serialize()
  
if __name__ == "__main__":
  att = Attribute()
  att.dom_attr_unit_test()
  