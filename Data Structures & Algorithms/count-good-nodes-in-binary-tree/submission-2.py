# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.sol = 0
        cm = root.val
        def dfs(root, cm):
            if root is None:
                return
            if root.val >= cm:
                self.sol+=1
            
            cm = max(cm, root.val)

            dfs(root.right, cm)
            dfs(root.left, cm)
        
        dfs(root, cm)
        return self.sol
            
            