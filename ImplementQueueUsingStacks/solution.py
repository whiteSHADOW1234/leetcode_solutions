class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        # move all the stuff in s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # add the element to s1 (which is an empty stack now)
        self.s1.append(x)

        # move all the element in s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()





# Best Solution thats most operation only works on out_stack
# class MyQueue:
#     def __init__(self):
#         # Initialize two empty stacks
#         self.in_stack = []
#         self.out_stack = []

#     def push(self, x: int) -> None:
#         # Append the new element to the in_stack
#         self.in_stack.append(x)

#     def _move_items(self):
#         # Helper method to move all elements from in_stack to out_stack
#         # if out_stack is empty
#         if not self.out_stack:
#             while self.in_stack:
#                 self.out_stack.append(self.in_stack.pop())

#     def pop(self) -> int:
#         # Ensure that out_stack contains the oldest element by
#         # moving elements from in_stack to out_stack if necessary
#         self._move_items()
#         # Pop the oldest element from out_stack
#         return self.out_stack.pop()

#     def peek(self) -> int:
#         # Ensure that out_stack contains the oldest element by
#         # moving elements from in_stack to out_stack if necessary
#         self._move_items()
#         # Return the oldest element without removing it
#         return self.out_stack[-1]

#     def empty(self) -> bool:
#         # The queue is considered empty if both in_stack and out_stack are empty
#         return not (self.in_stack or self.out_stack)
