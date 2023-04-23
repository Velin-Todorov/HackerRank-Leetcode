from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:

    def custom_comp(s1, s2):
        if s1+s2 > s2+s1:
            return -1
        else:
            return 1

    ns = [str(num) for num in nums]
    result = ''.join(sorted(ns, key=cmp_to_key(custom_comp))).lstrip('0')
    return result if len(result) != 0 else '0'
