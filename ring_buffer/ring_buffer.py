class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    print("current value:",self.current)
    print("store:", self.storage)
    if self.current <= len(self.storage) -1:
      self.storage[self.current] = item
      self.current += 1 
    else: 
      self.current = 0
      self.append(item)

  def get(self):
    request = []
    
    for i in self.storage:
      if i is not None:
        request.append(i)
    return request



#tests
buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')
print("Get =>",buffer.get())