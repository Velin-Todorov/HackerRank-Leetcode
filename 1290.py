#!/usr/bin/python3


def getDecimalValue(self, head: ListNode) -> int:

    temp = head
    res = ''
    while temp is not None:
        res += str(temp.val)
        temp = temp.next
        
    return int(res, base=2)
