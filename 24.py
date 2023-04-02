from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        remaining = head.next.next
        temp = head.next
        temp.next = head
        
        head.next = self.swapPairs(remaining)
        
        return temp