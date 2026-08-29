class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Pad grid by +1 so 0 represents empty string
        lc = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Note: 1-based indexing in DP corresponds to 0-based in strings
                if text1[i - 1] == text2[j - 1]:
                    lc[i][j] = 1 + lc[i - 1][j - 1]
                else:
                    lc[i][j] = max(lc[i - 1][j], lc[i][j - 1])

        return lc[m][n]