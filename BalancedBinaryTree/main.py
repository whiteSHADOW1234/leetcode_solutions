from solution import Solution, TreeNode


def main():
    # create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)


    #           1
    #          /  \
    #         2     2
    #        / \  
    #       3   3 
    #      / \
    #     4   4
    

    # check if the tree is balanced
    solution = Solution()
    is_balanced = solution.isBalanced(root)
    print(is_balanced)  # expected output: False


if __name__ == '__main__':
    main()
