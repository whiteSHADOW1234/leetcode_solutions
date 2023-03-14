from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute force solution Time: O(n) Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prevnode = head, None
        while current:
            temp = current.next
            current.next = prevnode
            prevnode = current
            current = temp
        return prevnode






# More complex solution using recursion Time: O(n) Space: O(n)
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Check if the head node is None (i.e., the list is empty)
#         if not head:
#             # If so, return None
#             return None

#         # Set a new variable called newHead to the current head node
#         newHead = head
        
#         # Check if there is more than one node in the list
#         if head.next:
#             # If so, recursively call the reverseList method on the next node in the list and set the returned node to newHead
#             newHead = self.reverseList(head.next)
#             # Set the next node of the next node to the current node (i.e., reverse the order of the nodes)
#             head.next.next = head
        
#         # Set the next node of the current node to None (i.e., set the tail of the reversed list)
#         head.next = None
        
#         # Return the new head node of the reversed list
#         return newHead
