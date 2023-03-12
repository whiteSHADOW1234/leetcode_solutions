from solution import Solution, TreeNode

# create a sample binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

#           4
#          / \ 
#         2   7
#        / \ / \
#       1  3 6  9

# create an instance of the Solution class
sol = Solution()

# invert the binary tree
inverted_tree = sol.invertTree(root)

# print the inverted tree (in preorder traversal)
def print_preorder(root: TreeNode) -> None:
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

print_preorder(inverted_tree)

#       4
#      / \
#     7   2
#    / \ / \
#   9  6 3  1
