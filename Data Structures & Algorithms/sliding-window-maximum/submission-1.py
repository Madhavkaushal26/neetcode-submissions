class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        res = []
        while r<len(nums):
            if r-l+1 >k:
                l+=1
            temp = nums[l:r+1]
            res.append(max(temp))
            r+=1
        return res