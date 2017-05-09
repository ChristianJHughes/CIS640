import math

class Queue(object):
  def __init__(self):   # default no-arg constructor
    self.items = []

  def enqueue(self, v): # adds v to the back of the queue; no return value
    if v == None or (isinstance(v, float) and math.isinf(v)) or (isinstance(v, float) and math.isnan(v)):
        raise ValueError()
    else:
        self.items.insert(0,v)

  def dequeue(self):    # removes and returns the element at the front of the queue
    if len(self.items) == 0:
        return None
    else:
        return self.items.pop()

  def len(self):        # returns the number of elements in the queue
    #assert isinstance(ret_val, int)
    return len(self.items)
