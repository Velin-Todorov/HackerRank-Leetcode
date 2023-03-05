#!/usr/bin/python3

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lst = []

        while temp is not None:
            lst.append(temp.val)
            temp = temp.next

        def insertionSort(arr):
            """Performs the insertion sort"""
            for i in range(1, len(arr)):
                current = arr[i]
                j = i - 1

                while j >= 0 and arr[j] > current:
                    arr[j + 1] = arr[j]
                    j -= 1
                
                arr[j + 1] = current
            
            return arr

        lst = insertionSort(lst)

        ll = ListNode(lst[0])
        head = ll

        def insert_in_ll(head, value):
            """Building new LL"""
            new_node = ListNode(value)
            temp = head
            
            if temp is None:
                new_node.next = temp
                head = new_node

            while temp.next is not None:
                temp = temp.next
            
            temp.next = new_node

            return head

        for i in insertionSort(lst)[1:]:
            head = insert_in_ll(head, i)
        
        return head


