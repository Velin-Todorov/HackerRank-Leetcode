#!/usr/bin/python3
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    temp1 = list1
    temp2 = list2

    lst = []

    if not list1 and not list2:
        return list1
    
    if not list1 and list2:
        return list2

    if not list2 and list1:
        return list1
 
    while temp1:
        lst.append(temp1.val)
        temp1 = temp1.next

    while temp2:
        lst.append(temp2.val)
        temp2 = temp2.next

    lst.sort()
    head = ListNode(val=lst[0])

    def insert(head, value):
        temp = head

        if temp is None:
            new_node = ListNode(value)
            new_node.next = temp.next
            head = new_node
        
        while temp.next is not None:
            temp = temp.next
        
        temp.next = ListNode(value)

        return head

    for i in lst[1:]:
        head = insert(head, i)


    return head

