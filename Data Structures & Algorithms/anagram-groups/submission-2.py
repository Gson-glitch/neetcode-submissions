from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) == 0: 
            return [[""]]

        hash_map = defaultdict(list)
        for s in strs:
            hash_map["".join(sorted(s))].append(s)

        return hash_map.values()