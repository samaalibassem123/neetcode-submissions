class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        open_brackets = ["{", "(", "["]
        closing_brackets = {"{":"}", "[":"]", "(":")"}
        stack = []
        for i in range(len(s)):
            if s[i] in open_brackets:
                stack.append(s[i])
            elif len(stack)  == 0:
                return False
            elif closing_brackets[stack[len(stack)-1]] == s[i]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True
