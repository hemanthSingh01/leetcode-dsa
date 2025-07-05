# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1=list1
        p2=list2
        if p1.val < p2.val:
            head=p1
            t=p1
            p1=p1.next
        else:
            head=p2
            t=p2
            p2=p2.next
        while p1 and p2:
            if p1.val < p2.val:
                t.next=p1
                p1=p1.next
                t=t.next
            else:
                t.next=p2
                p2=p2.next
                t=t.next
        if p1 is None:
            t.next=p2
        else:
            t.next=p1
        return head