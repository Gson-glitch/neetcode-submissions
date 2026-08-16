class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = [w.lower() for w in s if w.isalnum()]
        return parsed == parsed[::-1]