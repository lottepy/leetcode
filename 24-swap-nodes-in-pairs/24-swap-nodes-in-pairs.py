# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        swap = ListNode(None)
        res = swap
        count = 0
        while head is not None:
            if head.next is None:
                swap.next = head
                head = head.next
            else:
                swap.next = ListNode(head.next.val)
                swap.next.next = ListNode(head.val)
                head = head.next.next
                swap = swap.next.next

        return res.next        
            