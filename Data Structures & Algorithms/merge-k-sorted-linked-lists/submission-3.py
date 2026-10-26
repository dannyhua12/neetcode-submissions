# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(curr, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy

        while curr:
            val, i, node = heapq.heappop(curr)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(curr, (node.next.val, i, node.next))
        
        return dummy.next