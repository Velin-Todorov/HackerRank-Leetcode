#!/usr/bin/python3
"""https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?isFullScreen=true"""

def reverse(head):
    current = head
    prev = None

    while current is not None:
        current_next = current.next
        current.next = prev
        prev = current
        current = current_next

    head = prev

    return head


