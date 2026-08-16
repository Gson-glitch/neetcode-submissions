class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)]
        res = []

        for n in nums:
            hash_map[n] += 1

        for n, c in hash_map.items():
            bucket[c].append(n)

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res