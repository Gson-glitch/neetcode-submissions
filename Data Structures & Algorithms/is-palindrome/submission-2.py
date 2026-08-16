class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(map(lambda x: x.lower(), s.split()))
        string = "".join(filter(lambda x: x.isalnum(), list(string)))
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1

        return True