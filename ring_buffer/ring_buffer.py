class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    print("current value:",self.current)
    print("store:", self.storage)
    self.storage[self.current] = item
    if self.current < self.capacity -1:
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