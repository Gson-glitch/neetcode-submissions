from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        window = []

        for r in range(len(s)):
            window.append(s[r])
            if len(window) - Counter(window).most_common()[0][1] <= k:
                longest = max(longest, len(window))
            else:
                window.remove(s[l])
                l += 1

        return longest