class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        ops = 0

        while set(nums) != {0}:
            min_el = min([x for x in nums if x != 0])
            nums = [x - min_el for x in nums if x != 0]
            ops +=1
        
        return ops