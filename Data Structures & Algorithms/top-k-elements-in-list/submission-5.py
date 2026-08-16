class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = Counter(nums).most_common()[:k]
        return [num for num, count in top_k]