class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        suma = 0

        for i in range(len(self.nums)):
            
            suma += self.nums[i] * vec.nums[i]

        return suma