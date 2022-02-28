class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged   
        return lists[0]    

    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        merge = ListNode(None)      
        res = merge
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merge.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merge.next = ListNode(list2.val)
                list2 = list2.next
            merge = merge.next

        if list1 is not None:
            merge.next = list1
        if list2 is not None:
            merge.next = list2
        return res.next        