import random, os, sys

sys.path.append(os.getcwd()+"/core/")
import util

class JS_RANGE():

  def __init__(self):
    self.range_create_range = [
      "document.createRange()",
      "new Range()"
    ]
    self.range_create_helper= "function helper_create_range(rg,r1,r2,nd1,nd2) {\
      switch(r1%4) {\
        case 0: try{rg.setStartBefore(nd1);rg.setEndAfter(nd2);break; }catch(exception){}\
   		case 1: try{rg.setStart(nd1,0);rg.setEnd(nd2,0);break; }catch(exception){}\
   		case 2: try{rg.selectNode(nd1);break; }catch(exception){}\
   		case 3: try{rg.selectNodeContents(nd1);break;}catch(exception){}\
   		try{rg.selectNode(rNode());}catch(exception){}\
  	  }}"
    self.range_init_range = [
  	  "tmp_rg=%s;tmp_rg.setStartBefore($$[JSRandObj??LorR==rvalue&&type==Node]);tmp_rg.setEndAfter($$[JSRandObj??LorR==rvalue&&type==Node]);",
  	  "tmp_rg=%s;tmp_rg.setStart($$[JSRandObj??LorR==rvalue&&type==Node],0);tmp_rg.setEnd($$[JSRandObj??LorR==rvalue&&type==Node],0);",
  	  "tmp_rg=%s;tmp_rg.selectNode($$[JSRandObj??LorR==rvalue&&type==Node]);",
      "tmp_rg=%s;tmp_rg.selectNodeContents($$[JSRandObj??LorR==rvalue&&type==Node]);",
      #"range_create_helper($$[JSRandObj??LorR==lvalue&&type==Range],)"
    ]
    self.range_gao_range = {
  		"%s.$$[DOMExec];":5,
  		"%s.surroundContents($$[JSRandObj??LorR==rvalue&&type==Node]);":2,
  		"%s.insertNode($$[JSRandObj??LorR==rvalue&&type==Node]);":2,
  		"%s.deleteContents();":2,
  		"%s.detach();":3,
	}

  def create_range(self):
    return random.choice(self.range_create_range)

  def init_range(self, myRange=None):
    myRange = "$$[JSRandObj??LorR==lvalue&&type==Range]" if not myRange else myRange
    return random.choice(self.range_init_range) % (myRange)

  def gao_range(self, myRange=None):
    myRange = "$$[JSRandObj??LorR==rvalue&&type==Range]" if not myRange else myRange
    return util.w_choice(self.range_gao_range) % (myRange)

  # $$[Range??action==init&&myRange==Range_pre_0]
  # $$[Range??action==gao&&myRange==Range_pre_0]
  def DoRange(self, params):
    if not params:
      return None
    if "action" in params:
      if params["action"] == "init":
        return self.init_range(params["myRange"] if "myRange" in params else None)
      if params["action"] == "gao":
        return self.gao_range(params["myRange"] if "myRange" in params else None)

  def unit_test(self):
    print "[+] JS RANGE Test"
    print self.DoRange({"action":"init"})
    print self.DoRange({"action":"gao"})
    return self