class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        stack = []
        res = [0]*len(temp)
        
        for i,t in enumerate(temp):
            while stack and t>stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = i- stackInd
            stack.append((t,i))
        return res
