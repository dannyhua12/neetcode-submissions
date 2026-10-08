# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        track = deque([root])
        
        if root is None:
            return []
        while track:
            level = []
            for i in range(len(track)):
                value = track.popleft()
                level.append(value.val)
                if value.left:
                    track.append(value.left)
                
                if value.right:
                    track.append(value.right)
            
            res.append(level)
        
        return res