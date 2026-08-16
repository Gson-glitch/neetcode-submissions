class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for c in s:
            if c.isalnum():
                s_list.append(c.lower())
        s_reversed = s_list[::-1]
        if s_list == s_reversed:
            return True
        else:
            return False