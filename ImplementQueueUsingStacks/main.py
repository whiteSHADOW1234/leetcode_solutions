from solution import MyQueue

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())  # prints 1
print(q.pop())   # prints 1
print(q.empty()) # prints False
print(q.pop())   # prints 2
print(q.pop())   # prints 3
print(q.empty()) # prints True
