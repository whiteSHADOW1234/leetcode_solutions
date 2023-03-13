from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balance, 1 + max(left[1], right[1])]
        return dfs(root)[0]

# the code more readable and easier to understand
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def calculate_balance(node: Optional[TreeNode]) -> [bool, int]:
#             """
#             Calculate the balance and height of a binary tree.

#             :param node: The root of the binary tree to check
#             :return: A tuple containing a boolean indicating if the tree is balanced and the height of the tree
#             """
#             if not node:
#                 return [True, 0]
#             left_balance, left_height = calculate_balance(node.left)
#             right_balance, right_height = calculate_balance(node.right)
#             is_balanced = left_balance and right_balance and abs(left_height - right_height) <= 1
#             return [is_balanced, 1 + max(left_height, right_height)]

#         return calculate_balance(root)[0]
