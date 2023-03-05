#!/usr/bin/python3

def insertionSort(n, arr):
    for i in range(1, n):
        current = arr[i] #the current element

        j = i - 1

        while j >= 0 and arr[j] > current: #here we check if the element left to the current el is bigger. If yes:
            arr[j + 1] = arr[j] #We shift the left element to the right and there is a gap in the array
            j -= 1 #We move to the next left element, until we reach 0 or until we current is bigger that than the left element

        arr[j + 1] = current # fill the gap with the current_element

