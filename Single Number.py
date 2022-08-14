from collections import deque, Counter
from functools import reduce
from operator import xor


def singleNumber(nums):
        # return reduce(xor, nums) - Another solution

    deque_nums = deque(nums)
    idx = 0
    result = 0
    while True:

        if len(deque_nums) == 1:
            break

        if deque_nums[idx] == deque_nums[idx + 1]:
            deque_nums.popleft()
            deque_nums.popleft()
            idx = 0

    return deque_nums[0]

print(singleNumber([4,1,2,1,2]))