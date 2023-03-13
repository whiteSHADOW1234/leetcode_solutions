from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# the code more readable and easier to understand
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         """
#         Check if a singly-linked list contains a cycle.

#         :param head: The head of the linked list to check
#         :return: True if the linked list contains a cycle, False otherwise
#         """
#         slow_pointer, fast_pointer = head, head
#         while fast_pointer and fast_pointer.next:
#             slow_pointer = slow_pointer.next
#             fast_pointer = fast_pointer.next.next
#             if slow_pointer == fast_pointer:
#                 return True
#         return False
