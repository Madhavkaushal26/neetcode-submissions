class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0
        for i in prices:
            profit = i-minP
            res = max(profit,res)
            minP = min(minP,i)
        return res