#!/usr/bin/python3

def insertionSort(n, arr):
    for i in range(1, n):
        current = arr[i] #the current element

        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

