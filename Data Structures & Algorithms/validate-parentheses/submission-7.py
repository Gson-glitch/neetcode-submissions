class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {
            ']': '[', 
            ')': '(', 
            '}': '{'
        }

        for b in s:
            if b in pairs.values():
                stack.append(b)
            else:
                if stack and pairs[b] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0