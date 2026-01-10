#!/usr/bin/python3

#stack operation

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())

print(stack)


#LifoQueue

from queue import LifoQueue

stack = LifoQueue()

# Push elements
stack.put(10)
stack.put(20)
stack.put(30)

# Pop element
print(stack.get())  # Output: 30


#using class stack


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
s = Stack()
s.push(10)
print("print 10:", s)
s.push(20)
print("print 10 and 20:", s)
print(s.pop())  # Output: 20
