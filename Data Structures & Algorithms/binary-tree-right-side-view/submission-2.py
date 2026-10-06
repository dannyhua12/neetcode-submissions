# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return []

        track = deque([root])

        while track:
            levelSize = len(track)
            for i in range(levelSize):
                temp = track.popleft()
                if i == levelSize-1:
                    res.append(temp.val)
                if temp.left:
                    track.append(temp.left)
                if temp.right:
                    track.append(temp.right)
        
        return res
