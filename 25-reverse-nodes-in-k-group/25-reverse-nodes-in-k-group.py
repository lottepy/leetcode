# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        res = ListNode(0, head)
        prev, curr = res, head

        def updateK(curr):
            next = dict()
            i = 1
            next[i] = curr
            while i < k:
                if curr and curr.next:
                    curr = curr.next
                    next[i+1] = curr
                    i += 1
                else:
                    return None
            return next      
        
        next = updateK(curr)
        if not next:
            return res.next

        followingK = next[k].next
        while next[k]:
            # Change pointers
            for j in range(k, 1, -1):
                next[j].next = next[j - 1] 
            curr.next = followingK
            prev.next = next[k]
        
            # Re-Initiate
            prev = curr
            curr = followingK
            next = updateK(curr)       
            if not next:
                return res.next
            followingK = next[k].next

        return res.next 