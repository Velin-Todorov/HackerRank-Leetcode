#!/usr/bin/python3
"""https://www.hackerrank.com/challenges/find-the-median/problem?isFullScreen=true"""

def partition(arr, low, high):
    pivot  = arr[high]
    
    i = low - 1

    
    for j in range(low, high):
        
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


def quickSort(arr, low, high):
    
    if low < high:
    
        pivot = partition(arr, low, high)
    
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
                

def findMedian(arr):
    low = 0
    high = len(arr) - 1
    
    quickSort(arr, low, high)
    
    print(arr)
    return arr[(low + high) // 2]
