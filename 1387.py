#!/usr/bin/python3

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []
        for i in range(lo, hi + 1):
            power = 0
            x = i
            while x != 1:
                if x % 2 == 0:
                    x = x / 2 
                else:
                    x = (x * 3) + 1
                power +=1 
            arr.append((i, power))
        
        res = list(sorted(arr, key=lambda x: x[1]))
        return res[k - 1][0]


