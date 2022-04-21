# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None, head)
        newHead = prev
        while head is not None and head.next is not None:
            if head.val != prev.val:
                prev = head
                head = head.next
            else: # head.val == prev.val
                prev.next = head.next
                head = head.next
        if head is not None and head.val == prev.val:
            prev.next = None        
        return newHead.next   