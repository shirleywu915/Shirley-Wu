class Player:
  def __init__(self, dealer=False):
    self.cards = [] #store the actual cards
    self.sum = 0 #store point sum

class card:
  def __init__(self,filename,value,label=None):
    self.filename = filename
    self.value = value
    self.label = label
