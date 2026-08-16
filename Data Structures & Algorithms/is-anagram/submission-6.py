class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        counter_s, counter_t = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            counter_s[s[i]] += 1
            counter_t[t[i]] += 1

        for key, val in counter_s.items():
            if val != counter_t[key]:
                return False

        return True


        