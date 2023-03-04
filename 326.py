#!/usr/bin/python3

def isPowerOfThree(n: int):

    if n <= 1:
        return n == 1

    number = isPowerOfThree(n//3)
    return (n%3 == 0 and number)

