class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(map(lambda x: x.strip().lower() if x.isalnum() else "", s))
        s_str = "".join(s_list)
        return s_str == s_str[::-1]