from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            index = nums.index(n)
            new_list = nums[:index] + nums[index+1:]
            res.append(prod(new_list))

        return res
            
        