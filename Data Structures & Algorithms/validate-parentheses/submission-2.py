class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        def getMatch(char: str) -> str | None:
            if char == ')':
                return opening[0]
            if char == '}':
                return opening[1]
            if char == ']':
                return opening[2]

        for i in range(len(s)):
            char = s[i]
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0 or getMatch(char) != stack[-1]:
                    return False
                else:
                    stack.pop() 

        if len(stack) > 0:
            return False

        return True