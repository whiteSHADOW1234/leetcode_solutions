from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# Simple two-pointer solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# More readable solution
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Initialize two pointers, one moving twice as fast as the other
#         current: Optional[ListNode] = head
#         runner: Optional[ListNode] = head
#         # Traverse the linked list until the runner reaches the end
#         while runner and runner.next:
#             current = current.next
#             runner = runner.next.next
#         # Return the current node, which is the middle node
#         return current
