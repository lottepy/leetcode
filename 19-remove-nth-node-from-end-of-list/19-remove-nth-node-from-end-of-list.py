# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = copy.copy(head)
        forCount = copy.copy(head)
        prev = ListNode(None)
        prev.next = res
        count = 0
        while forCount.next is not None:
            forCount = forCount.next
            count += 1

        _count = 0
        while _count <= count - n:
            prev = prev.next
            head = head.next
            _count += 1

        prev.next = head.next
        if prev.val is None:
            return prev.next
        return res