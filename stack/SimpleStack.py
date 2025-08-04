class SimpleStack:

  def __init__(self):
    self.data = []


  def push(self, value: int):
    self.data.append(value)


  def pop(self):
    return self.data.pop()
  

  def peek(self):
    return self.data[-1]


stack = SimpleStack()
stack.push(10)
stack.push(55)
stack.push(13)

print(stack.peek())
print(stack.pop())
print(stack.peek())