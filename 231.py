#!/usr/bin/python3

def isPowerOfTwo(n: int):

    if n <= 1:
        return n==1

    output = isPowerOfTwo(n // 2)

    return (n % 2 == 0 and output)
