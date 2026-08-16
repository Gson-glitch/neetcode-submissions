class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_str = ""
        for c in s:
            if c.isalnum():
                s_str += c.lower()
        n = len(s_str)
        l, r = 0, n - 1
        while l <= r and l < n - 1:
            if s_str[l] == s_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
