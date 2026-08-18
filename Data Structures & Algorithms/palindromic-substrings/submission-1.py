class Solution:
    def countSubstrings(self, s: str) -> int:
        
        t = "^#" + "#".join(s) + "#$"

        n = len(t)
        c,r=0,0
        p = [0]*n

        for i in range(1,n-1):
            i_mir = 2*c -i

            if i<r:
                p[i] = min((r-i),p[i_mir])
            
            while t[i+1+p[i]] == t[i-1-p[i]]:
                p[i] +=1
            
            if i + p[i] > r:
                c = i
                r = i + p[i]

        res = 0
        for i in p:
            res += (i+1)//2
        return res
        