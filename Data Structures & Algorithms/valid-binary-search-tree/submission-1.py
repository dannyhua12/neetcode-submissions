# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = float('-inf')
        u = float('inf')
        def dfs(root, lower, upper):
            if root is None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            left = dfs(root.left, lower, root.val)
            right = dfs(root.right, root.val, upper)
            return left and right
        
        return dfs(root, l, u)