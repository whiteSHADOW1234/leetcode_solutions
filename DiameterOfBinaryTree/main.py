from solution import Solution, TreeNode

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

# Instantiate the Solution class
sol = Solution()

# Call the diameterOfBinaryTree() method with the root of the binary tree
diameter = sol.diameterOfBinaryTree(root)

# Print the diameter of the binary tree
print("The diameter of the binary tree is:", diameter)

