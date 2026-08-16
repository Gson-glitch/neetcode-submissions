from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        for r in range(len(s1)-1, len(s2)):
            sub_string = s2[l: r+1]
            if Counter(s1) == Counter(sub_string):
                return True
            l += 1

        return False