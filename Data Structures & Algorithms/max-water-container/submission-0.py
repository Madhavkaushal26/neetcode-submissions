class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        maxv = 0
        while l<len(heights)-1:
            r = len(heights)-1
            while r>l:
                vol = min(heights[l],heights[r])*(r-l)
                maxv = max(maxv,vol)
                r-=1
            l+=1
        return maxv