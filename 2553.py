class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        res = []

        for i in nums:
            temp = list(str(i))
            res.extend(map(int, temp))

        
        return res