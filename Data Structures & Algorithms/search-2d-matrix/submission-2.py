class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows , cols = len(matrix) , len(matrix[0])

        l ,r = 0 , rows*cols-1

        while l<=r:
            m = (l + (r-l)//2)
            mr = m//cols
            mc = m%cols

            if matrix[mr][mc]<target:
                l = m+1
            elif matrix[mr][mc]>target:
                r = m-1
            else:
                return True
        return False
