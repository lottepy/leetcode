# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        left, right = head, head
        res = left
        count = 1
        kMemo = k
        while k > 0:
            if right.next:
                right = right.next
                k -= 1
                count += 1
            else:
                right = head
                k = kMemo % count
                

        while right.next:
            left = left.next
            right = right.next    
        tmp = left.next
        left.next = None  
        if tmp:
            rotate = tmp
            while tmp.next:
                tmp = tmp.next
            tmp.next = res
            return rotate
        else:
            return res    
   