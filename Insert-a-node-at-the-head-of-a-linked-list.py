#!/usr/bin/python3

def insertNodeAtHead(llist, data):
    temp = llist
    new_node = SinglyLinkedListNode(data)
    
    if llist is None:
        return new_node
    
    new_node.next = temp
    llist = new_node

    
    return llist


