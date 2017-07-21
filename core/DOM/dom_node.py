import random, collections

class Node(object):
    def __init__(self, tag, attrib=None, css=None, event=None):
        self.tag = tag
        self.id = ""
        self.body_before = ""
        self.body_btw = ""
        self.body_after = ""
        self.parent = None
        self.children = []
        self.attrib = attrib
        self.css = css
        self.events = event

    def add_child(self, obj):
        if obj is None:
          return None
        obj.parent = self
        self.children.append(obj)

    def dump(self):
      return {"tag":    self.tag, 
              "parent": self.parent,
              "chidren":self.children}

    def get_must_have_attrib(self, cur_tag):
      self.attrib.fill_must_have_attrib(cur_tag)

    def pre_define_attr(self, attr_set):
      for attr in attr_set:
        if attr_set[attr]:
          self.attrib.insert_attrib(attr, attr_set[attr])
        else:
          self.attrib.fill_attrib(attr, attr_set[attr])

    def pre_define_css(self, css_set):
      for css in css_set:
        if css_set[css]:
          self.css.insert_css(css, css_set[css])
        else:
          self.css.fill_css(css, css_set[css])

    def serialize(self, with_Attr=True, with_CSS=True, with_Event=True, with_Class=True, depth=0):
      attr_str = ""
      if with_Attr:
        attr_str = self.attrib.serialize()
      event_str = ""
      #if with_Event:
      #  event_str = self.events.serialize()
      class_str =""
      if with_Class:
        class_str = "class=\"%s\"" % ("$$[dom_class_name] "*random.randint(0, 5))
      css_str = ""
      if with_CSS:
        css_str = self.css.serialize()
      str = "\n%s<%s id='%s' %s %s %s %s>%s" % ("\t"*depth, self.tag, self.id, attr_str, class_str, event_str, css_str, self.body_before)      
      if len(self.children)>0:
        for child in self.children:
          str += child.serialize(depth=depth+1)
      str += "%s\n</%s>" % (self.body_after, self.tag)
      return str

    def collect_info(self):
      info = {"used_tag_name":collections.Counter({})}
      for child in self.children:
        sub_info = child.collect_info()
        info["used_tag_name"] = collections.Counter(sub_info["used_tag_name"]) + info["used_tag_name"]
      if self.tag in info["used_tag_name"]:
        info["used_tag_name"][self.tag] = 0
      info["used_tag_name"][self.tag] += 1
      return info
      
    def dom_node_unit_test(self):
      print "\n[+] DOM Node Test"
      print self.serialize()