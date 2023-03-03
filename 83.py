#!/usr/bin/python3


def deleteDuplicates(head):
    if head is None:
        return 
        
    current = head
    temp = None
    index = None

    while current is not None:
        temp = current
        index = current.next

        while index is not None:
            
            if current.val == index.val:
                temp.next = index.next
            else:
                temp = index
            index = index.next
        current = current.next
    
    return head

