# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Return True if both Trees are empty
        if not p and not q:
            return True
        
        # Return False if at least one Tree is empty or the values don't match
        if not p or not q or p.val != q.val:
            return False

        # DFS on left and right subtrees
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))