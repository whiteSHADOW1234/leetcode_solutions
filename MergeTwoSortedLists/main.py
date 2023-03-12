from solution import Solution, ListNode

# Test the mergeTwoLists() function
if __name__ == '__main__':
    # Create some example linked lists
    l1 = ListNode(1, ListNode(2, ListNode(4))) # 1 -> 2 -> 4 -> None
    l2 = ListNode(1, ListNode(3, ListNode(4))) # 1 -> 3 -> 4 -> None

    # Merge the linked lists
    sol = Solution()
    merged_list = sol.mergeTwoLists(l1, l2)

    # Print the merged list
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print("None")