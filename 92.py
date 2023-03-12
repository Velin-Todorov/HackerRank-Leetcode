#!/usr/bin/python3

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp = head
        lst = []

        idx = 0

        while temp is not None:
            lst.append(temp.val)
            temp = temp.next

        lst_snip = lst[left -1: right]
        lst[left-1: right] = lst_snip[::-1]

        new_head = ListNode()
        temp = new_head

        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        
        return new_head.next

