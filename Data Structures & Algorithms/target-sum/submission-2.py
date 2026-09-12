class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (total+target)<0 or (total+target)%2!=0:
            return 0
        
        sub = (total+target)//2

        dp = [0]*(sub+1)
        dp[0] = 1

        for num in nums:
            for i in range(sub,num-1,-1):
                dp[i] += dp[i - num]
        
        return dp[sub]