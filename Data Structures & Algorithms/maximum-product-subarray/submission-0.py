class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        currMax = 1
        currMin = 1

        for curr in nums:
            temp = currMax*curr
            currMax = max(curr,currMax*curr,currMin*curr)
            currMin = min(curr,temp,currMin*curr)

            res = max(currMax,res)
        
        return(res)


        