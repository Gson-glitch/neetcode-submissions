class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inverse = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bracket in s:
            if bracket in inverse and stack:
                if stack[-1] == inverse[bracket]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(bracket)
        print(stack)
        return len(stack) == 0
