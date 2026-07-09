import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        stack = []
        for i in tokens:
            if i in ops:
                v2 = stack.pop()
                v1 = stack.pop()
                if i == "+":
                    stack.append(int(v1 + v2))
                elif i == "*":
                    stack.append(int(v1 * v2))
                elif i == "/":
                    stack.append(int(v1 / v2))
                elif i == "-":
                    stack.append(int(v1 - v2))
            else:
                stack.append(int(i))
        return stack[-1]