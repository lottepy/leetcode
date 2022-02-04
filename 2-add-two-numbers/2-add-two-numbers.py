# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        resList = ListNode(0, None)
        temp = resList
        while l1 is not None or l2 is not None or val //10 != 0:
            val = val // 10
            if l1 is not None:
                val += l1.val
            if l2 is not None:
                val += l2.val
            
            temp.next = ListNode(val=val % 10, next=None)
            temp = temp.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:    
                l2 = l2.next
        
        return resList.next
    
if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(9, None)
    l1.next = ListNode(9, None)

    
    l2 = ListNode(9, None)
    l2.next = ListNode(9, None)
    
    res = sol.addTwoNumbers(l1, l2)
    