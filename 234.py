#!/usr/bin/python3

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        cursor = 0

        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next

        return lst == lst[::-1]
