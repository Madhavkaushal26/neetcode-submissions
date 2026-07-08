class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        res = ""
        l = 0
        mincount = float('inf')
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
    
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)

            if c in countT and countT[c]==window[c]:
                have +=1
            while have==need:
                if (r-l+1)<mincount:
                    res = s[l:r+1]
                    mincount = min(mincount,r-l+1)
                
                window[s[l]] -=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have -=1
                l+=1

        return res if mincount!=float('inf') else ""