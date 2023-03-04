#!/usr/bin/python3

def middleNode(head):

    temp = head
    size = 0

    while temp is not None:
        size += 1
        temp = temp.next

    mid_el = size // 2
    
    count = 0

    node = None
    temp = head

    while temp is not None:
        if count == mid_el:
            node = temp
            break
        count += 1
        temp = temp.next
    
    if node:
        return node


