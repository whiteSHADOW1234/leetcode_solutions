from solution import Solution, ListNode


def main():
    # create a linked list with a cycle
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next  # create a cycle from node 4 to node 2

    # check if the linked list contains a cycle
    solution = Solution()
    has_cycle = solution.hasCycle(head)
    print(has_cycle)  # expected output: True


if __name__ == '__main__':
    main()
