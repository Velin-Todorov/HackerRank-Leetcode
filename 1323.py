class Solution:
    def maximum69Number (self, num: int) -> int:
        

        # print(set(str(num)))
        if set(str(num)) == {'9'}:
            return num
        
        
        lst = []
        nums = list(str(num))
        for i in range(len(nums)):
            if nums[i] == '6':
                nums[i] = '9'
                lst.append(nums)
                nums = list(str(num))

        res = int(''.join(max(lst)))
        return res
