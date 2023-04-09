def leftRigthDifference(self, nums: List[int]) -> List[int]:

        leftSum = [None] * len(nums)
        rightSum = [None] * len(nums)

        rightSum[-1] = 0
        leftSum[0] = 0

        result = [None] * len(nums)

        for i in range(1,len(nums)):
            #building leftsum
            leftSum[i] = sum(nums[:i])
            rightSum[-i - 1] = sum(nums[-i:])

        for i in range(len(nums)):
            result[i] = abs(leftSum[i] - rightSum[i])

        return result