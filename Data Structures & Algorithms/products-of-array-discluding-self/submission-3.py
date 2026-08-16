from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            extract = nums[:i] + nums[i+1:]
            res.append(reduce(lambda x, y: x*y, extract))

        return res