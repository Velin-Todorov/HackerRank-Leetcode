from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 0

        while nums:
            total += min(nums.pop(), nums.pop())
        
        return total
            