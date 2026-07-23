# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        track = deque([root])
        sol = []
        if root is None:
            return []

        while track:
            level = []
            levelSize = len(track)
            for i in range(levelSize):
                curr = track.popleft()
                level.append(curr.val)
                if curr.left:
                    track.append(curr.left)
                if curr.right:
                    track.append(curr.right)
                
            sol.append(level)
        
        return sol