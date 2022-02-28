# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # Method 1: Brute Force
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     swap = ListNode(None)
    #     res = swap
    #     while head is not None:
    #         if head.next is None:
    #             swap.next = head
    #             head = head.next
    #         else:
    #             swap.next = ListNode(head.next.val)
    #             swap.next.next = ListNode(head.val)
    #             head = head.next.next

    #     return res.next 

    # Method 2: Shift Pointers          
        def swapPairs(self, head: ListNode) -> ListNode: 
            res = ListNode(0, head)
            prev, curr = res, head
            while curr and curr.next:
                # Store pointers
                next = curr.next
                followingPair = curr.next.next

                # Change pointers
                next.next = curr
                prev.next = next
                curr.next = followingPair

                # Reassign
                prev = curr
                curr = followingPair

            return res.next