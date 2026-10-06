# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res =[]
        track = deque([root])

        while track:
            temp = []
            for i in range(len(track)):
                tempN = track.popleft()
                temp.append(tempN.val)
                if tempN.left:
                    track.append(tempN.left)
                if tempN.right:
                    track.append(tempN.right)
            
            res.append(temp)
        
        return res
                