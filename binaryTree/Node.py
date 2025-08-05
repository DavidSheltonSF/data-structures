from collections import deque



class Node:
  def __init__(self, value):
    self.value = value
    self.left: Node = None
    self.right: Node = None

  def print_in_order(self):
    if(self.left):
      self.left.print_in_order()
    print(self.value)
    if(self.right):
      self.right.print_in_order()

  def print_pre_order(self):
    print(self.value)
    if(self.left):
      self.left.print_pre_order()
    if(self.right):
      self.right.print_pre_order()

  def print_breadth_first_search(self, queue):
    print(self.value)
    if(self.left):
      queue.append(self.left)
    if(self.right):
      queue.append(self.right)

    if(len(queue) > 0):
      next = queue.popleft()
      next.print_breadth_first_search(queue)
    


root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.right.right = Node(14)
queue = deque()
root.print_breadth_first_search(queue)
