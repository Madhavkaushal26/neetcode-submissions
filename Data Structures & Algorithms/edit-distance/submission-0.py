class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS,COLS = len(word1),len(word2)

        dp = [[float('inf')]*(COLS+1) for _ in range(ROWS+1)]

        for i in range(ROWS+1):
            dp[i][COLS] = ROWS-i
        for i in range(COLS+1):
            dp[ROWS][i] = COLS-i
        
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    res = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1]) 
                    # min(insert, delete, update)
                    dp[i][j] = 1 + res
                
        return dp[0][0]
        