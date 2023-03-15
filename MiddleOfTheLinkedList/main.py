from typing import List
from solution import ListNode, Solution

def create_linked_list(nums: List[int]) -> ListNode:
    """Helper function to create a linked list from a list of integers."""
    head = ListNode()
    current = head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return head.next

if __name__ == '__main__':
    # Create a linked list [1, 2, 3, 4, 5]
    head = create_linked_list([1, 2, 3, 4, 5])
    # Create a Solution object and call the middleNode method on the linked list
    sol = Solution()
    middle = sol.middleNode(head)
    # Print the value of the middle node
    print(middle.val)
