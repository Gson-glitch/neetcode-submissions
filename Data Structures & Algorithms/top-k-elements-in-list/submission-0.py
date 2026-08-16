from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums)
        return [elem[0] for elem in counter_nums.most_common(k)]