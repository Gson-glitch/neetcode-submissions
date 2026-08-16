class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff]+1, i+1]
            hash_map[n] = i