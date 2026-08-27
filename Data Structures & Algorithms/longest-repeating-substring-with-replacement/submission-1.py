class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            # Add right character to frequency map
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            # If current window needs more than 'k' replacements, shrink window
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # Track max window length found so far
            res = max(res, r - l + 1)

        return res
        