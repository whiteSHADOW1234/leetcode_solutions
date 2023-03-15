from solution import Solution, TreeNode

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create a Solution object and call the maxDepth function on the root node
sol = Solution()
max_depth = sol.maxDepth(root)

# Print the result
print("Max depth:", max_depth)
