# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        track = deque([root])
        sol = []

        while track:
            levelSize = len(track)
            for i in range(levelSize):
                curr = track.popleft()
                if i == levelSize-1:
                    sol.append(curr.val)
                if curr.left:
                    track.append(curr.left)
                if curr.right:
                    track.append(curr.right)
        
        return sol