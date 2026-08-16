class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)

        for i in range(len(nums) - 1):
            # Skip duplicates for i in the outer loop
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates from the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicates from the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
