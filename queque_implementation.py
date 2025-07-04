# -*- coding: utf-8 -*-
"""queque_implementation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10M6NBA46taya2H5Jb0ig_C96xYE9A1e9
"""

class queque:
  def __init__(self):
    self.items=[]

  def is_empty(self):
    return self.items==None

  def enqueue(self,item):
    self.items.insert(0,item)

  def dequeue(self):
    if not self.is_empty():
      return self.items.pop()

  def size(self):
    return len(self.items)

  def get_front(self):
    if not self.is_empty():
      return self.items[-1]

  def get_rear(self):
    if not self.is_empty():
      return self.items[0]

q1=queque()
q1.enqueue(2)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.enqueue(9)
q1.enqueue(10)
print(q1.get_front())
print(q1.get_rear())
print(q1.size())

_