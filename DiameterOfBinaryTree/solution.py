from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution with integer variable to store the diameter
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return res


# Solution with list to store the diameter
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         res = [0]
#         def dfs(root):
#             if not root:
#                 return -1
#             left = dfs(root.left)
#             right = dfs(root.right)
#             res[0] = max(res[0], 2 + left +right)
#             return 1 + max(left, right)

#         dfs(root)
#         return res[0]
