class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class NodeStack:
  def __init__(self):
    self.top: Node = None
    self.size: int = 0


  def push(self, value):
    newNode = Node(value)
    newNode.next = self.top
    self.top = newNode
    self.size += 1


  def pop(self):
    if(self.is_empty()):
      return
    
    aux = self.top
    self.top = aux.next
    aux.next = None
    self.size -= 1
    return aux.data


  def printStack(self):
    current = self.top

    print('-' * 10)

    while(current is not None):
      print(current.data)
      current = current.next

    print('-' * 10)


  def is_empty(self):
    return self.size == 0



