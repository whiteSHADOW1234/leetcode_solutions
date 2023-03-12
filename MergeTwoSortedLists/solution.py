from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a single sorted linked list.

        Args:
            list1 (Optional[ListNode]): The head node of the first linked list.
            list2 (Optional[ListNode]): The head node of the second linked list.

        Returns:
            Optional[ListNode]: The head node of the merged linked list.
        """
        # Create a dummy node to serve as the head of the merged list
        head = ListNode()
        tail = head

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append any remaining nodes from either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the head of the merged list
        return head.next
