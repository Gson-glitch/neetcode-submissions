class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = {}
        for num in nums:
            counter_nums[str(num)] = counter_nums.get(str(num), 0) + 1
        return [int(item[0]) for item in sorted(counter_nums.items(), key=lambda x: x[1], reverse=True)[:k]]
    