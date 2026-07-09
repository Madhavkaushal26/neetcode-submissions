class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]":"[","}":"{",")":"("}
        if len(s)<=1:
            return False
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            else:
                if stack and stack[-1]==d[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
