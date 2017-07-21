import random

class Stack:
  def __init__(self):
         self.items = []

  def isEmpty(self):
         return self.items == []

  def push(self, item):
         self.items.append(item)

  def pop(self):
         return self.items.pop()

  def peek(self):
         return self.items[len(self.items)-1]

  def size(self):
         return len(self.items)
         
class jjjj:
  def __init__(self):
    self.stack = Stack()
    self.pairs = []
    self.load_config()
    
  def load_config(self, f="core/Heuristic/jjjj/jjjj.config"):
    file_jj = open(f, "r")
    patterns = file_jj.read().split("\n")
    for i in range(0, len(patterns), 2):
      self.pairs.append(patterns[i:i+2])

  def select_random_pair(self):
    return random.choice(self.pairs)
    
  def get_opening_pair(self, param={}):
    selected = self.select_random_pair()
    self.stack.push(selected[1])
    return selected[0]
  
  def get_closing_pair(self, param={}):
    return self.stack.pop()
    
  def fill_jjjj_tag(self, param={}):
    if random.randint(1, 10) > self.stack.size():
      return self.get_opening_pair(param)
    else:
      return self.get_closing_pair(param)
    
  def get_template_tag(self):
    return {
      "$$[jjjj" : {
        "impl" : self.fill_jjjj_tag,
        "help" : "heuristic jjjj",
        "i.e." : "",
      },
    }
def test():
  jj = jjjj()
  jj.load_config()
  print jj.stack.size()+1, jj.get_opening_pair()
  print jj.stack.size()+1, jj.get_opening_pair()
  print jj.stack.size(), jj.get_closing_pair()
  print jj.stack.size()+1, jj.get_opening_pair()
  print jj.stack.size()+1, jj.get_opening_pair()
  print jj.stack.size(), jj.get_closing_pair()
  print jj.stack.size(), jj.get_closing_pair()
  print jj.stack.size(), jj.get_closing_pair()
  
if __name__ == "__main__":
  test()