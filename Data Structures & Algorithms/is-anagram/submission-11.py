from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s, hash_t = defaultdict(int), defaultdict(int)
        
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            hash_s[char_s] += 1
            hash_t[char_t] += 1

        return hash_s == hash_t
