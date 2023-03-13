from typing import Optional


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur




