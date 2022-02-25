# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # # Method 1: Brute Force
    #     res = copy.copy(head)
    #     forCount = copy.copy(head)
    #     prev = ListNode(None)
    #     prev.next = res
    #     count = 0
    #     while forCount.next is not None:
    #         forCount = forCount.next
    #         count += 1

    #     _count = 0
    #     while _count <= count - n:
    #         prev = prev.next
    #         head = head.next
    #         _count += 1

    #     prev.next = head.next
    #     if prev.val is None:
    #         return prev.next
    #     return res
    
    # Method 2: Two Pointers    
        front, end = 1, 1
        _head = ListNode(None)
        _head.next = head
        res = _head
        tail = copy.deepcopy(head)
        while end - front <= n:
            if end - front == n and tail is not None:
                _head = _head.next
                front += 1
            elif end - front == n and tail is None:
                _head.next = _head.next.next
                return res.next
            tail = tail.next 
            end += 1
        return None        