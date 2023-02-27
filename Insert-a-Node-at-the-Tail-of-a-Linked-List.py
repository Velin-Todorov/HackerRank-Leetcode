#!/usr/bin/python3

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    temp = head
    
    if temp is None:
        head = new_node
        return head

    while temp.next is not None:
        temp = temp.next
    
    temp.next = new_node
    return head

