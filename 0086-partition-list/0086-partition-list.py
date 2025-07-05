# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1=ListNode()
        l2=ListNode()
        temp1=l1
        temp2=l2
        curr=head
        while curr:
            if curr.val>=x:
                temp2.next=curr
                temp2=temp2.next
            elif curr.val < x:
                temp1.next=curr
                temp1=temp1.next
            curr=curr.next
        temp2.next=None
        temp1.next=l2.next
        return l1.next