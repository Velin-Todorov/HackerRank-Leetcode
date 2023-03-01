#!/usr/bin/python3

def reverseList(self, head):
    prev = None
    current = head

    while current is not None:
        current_next = current.next
        current.next = prev
        prev = current
        current = current_next

    head = prev

    return head


