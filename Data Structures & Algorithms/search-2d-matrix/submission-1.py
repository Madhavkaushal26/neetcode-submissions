class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l = 0
        r = len(matrix[0])-1
        row = 0 
        while row<len(matrix) and l<=r:
            m = l + (r-l)//2
            if matrix[row][len(matrix[row])-1]<target:
                row+=1
                l = 0
                r = len(matrix[0])-1
                continue
            if matrix[row][m]==target:
                return True 

            elif matrix[row][m]<target:
                l = m+1

            else:
                r = m-1
            
        if l > r:
                return False
                
        return False 
    
