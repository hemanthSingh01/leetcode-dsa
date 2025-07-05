class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_dummy = ListNode()
        even_dummy = ListNode()
        odd, even = odd_dummy, even_dummy
        curr = head
        index = 1
        
        while curr:
            if index % 2 != 0:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            curr = curr.next
            index += 1
        
        odd.next = None
        even.next = None

        odd, even = odd_dummy.next, even_dummy.next
        new_head = even_dummy.next if even_dummy.next else odd_dummy.next
        
        if not even:
            return odd
        
        temp = None
        while even:
            temp = even
            next_even = even.next
            next_odd = odd.next if odd else None
            
            even.next = odd
            
            if next_even:
                odd.next = next_even
            else:
                odd.next = next_odd
            
            even = next_even
            odd = next_odd
        
        return new_head
