class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = "".join(s.split()).lower()
        filtered_s = list(filter(lambda x: x.isalnum(), lower_s))
        final = "".join(filtered_s)
        return final == final[::-1]