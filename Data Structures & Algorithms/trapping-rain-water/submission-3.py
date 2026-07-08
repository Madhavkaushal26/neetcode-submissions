class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        vol = 0
        leftMax, rightMax = height[l], height[r]
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                vol += leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                vol += rightMax-height[r] 

        return vol