class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l , r = 1,max(piles)
        res = r

        while l<=r:
            k = l+ (r-l)//2

            Tt = 0
            for p in piles: 
                Tt += math.ceil(float(p)/k)

            if Tt <=h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
