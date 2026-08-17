class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        t = "^#" + "#".join(s) + "#$"
        max_len = 0
        center_idx = 0

        n = len(t)
        p = [0]*n
        c,r = 0,0

        for i in range(1,n-1):
            i_mirror = 2 * c - i
            if i<r:
                p[i] = min((i-r),i_mirror)
            
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > r:
                c = i
                r = i + p[i]
            
            if p[i] > max_len:
                max_len = p[i]
                center_idx = i
        start = (center_idx - max_len) // 2
        return s[start : start + max_len]