class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            curr = strs[i]
            while not curr.startswith(prefix) and prefix:
                prefix = prefix[:-1]

        return prefix if prefix else ""
