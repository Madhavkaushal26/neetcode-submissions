class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        n = len(prices)
        # dp[i][0]: hold, dp[i][1]: sold, dp[i][2]: rest
        dp = [[0] * 3 for _ in range(n)]
        
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
            
        return max(dp[n-1][1], dp[n-1][2])