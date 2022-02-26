# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif (list1 is None and list2 is not None) or (list1 is not None and list2 is not None and list1.val > list2.val):
            return self.mergeTwoLists(list2, list1)
        anchor1, anchor2 = list1, list2       
        res = anchor1
        while anchor1 is not None and anchor2 is not None:  
            if anchor1.val <= anchor2.val:
                if anchor1.next is None:
                    anchor1.next = anchor2
                    anchor2 = None
                elif anchor2.val <= anchor1.next.val:    
                    temp = copy.deepcopy(anchor1.next)
                    anchor1.next = ListNode(anchor2.val)
                    anchor1.next.next = temp
                    anchor1 = anchor1.next
                    anchor2 = anchor2.next  
                else:
                    anchor1 = anchor1.next    
            else: # anchor1.val > anchor2.val
                pass

        return res          


if __name__ == '__main__':
    list1 = ListNode(-9)
    list1.next = ListNode(3)
    # list1.next.next = ListNode(4)
    list2 = ListNode(5)
    list2.next = ListNode(7)
    # list2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(list1, list2))