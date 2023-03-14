from typing import List
from solution import ListNode, Solution

def create_linked_list(arr: List[int]) -> ListNode:
    # Create a linked list from an array of integers
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def print_linked_list(head: ListNode):
    # Print the values of a linked list
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Example usage:
    arr = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(arr)
    solution = Solution()
    reversed_list = solution.reverseList(linked_list)
    print_linked_list(reversed_list) # prints "5 4 3 2 1"
