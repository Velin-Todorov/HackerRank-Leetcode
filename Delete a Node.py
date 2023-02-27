#!/usr/bin/python3

def deleteNode(llist, position):
    # Write your code here
    
    #llist is the head of the LL

    prev = position - 1 #find the position of the previous element
    temp = llist
    
    count = 0
    
    if position == 0:
        ahead = temp.next
        llist = ahead
        return llist
    
    previous = None
    
    while temp.next is not None:
        if prev == count:
            previous = temp
            break
            
        count += 1
        temp = temp.next

    if previous: #if previous element is found
        ahead = previous.next.next #get the pointer of the previous's next.
        previous.next = ahead #set the pointer of the previous's next to ahead. We have deleted the previous next, because there are no more references to it.
        
        
    return llist
