class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        def mat_mult(A,B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                     A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                     A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

        def mat_pow(A,p):
            res = [[1,0],[0,1]]
            base = A

            while p:
                if p%2==1:
                    res = mat_mult(res,base)
                base = mat_mult(base,base)
                p //= 2
            
            return res
        M = [[1,1],[1,0]]
        res = mat_pow(M,n)
        return res[0][0]