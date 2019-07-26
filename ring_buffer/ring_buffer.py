class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    print("current value:",self.current)
    self.storage[self.current] = item
    if self.current < self.capacity -1:
      self.current += 1
    else:
      self.current = 0
    #should reset it

  def get(self):
    request = []
    for i in self.storage:
      if i is not None:
        request.append(i)
      return request
      print(request)