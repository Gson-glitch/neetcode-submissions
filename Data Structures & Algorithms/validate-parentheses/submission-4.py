class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inverse = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for c in s:
            if c in inverse:
                if stack and stack[-1] == inverse[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
