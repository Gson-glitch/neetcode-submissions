import re

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        sep = "#"
        for s in strs:
            len_s = len(s)
            encoded_str += str(len_s) + sep
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        pattern = re.compile(r"(\d+)#")
        res = []
        i = 0

        while i < len(s):
            match = pattern.match(s, i)
            length = int(match.groups()[0])
            end = match.end()
            res.append(s[end: end+length])
            i = end+length

        return res

            
        

