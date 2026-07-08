class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = {}
        for i,n in enumerate(numbers):
            if n not in dic:
                dic[target-n]=i
            else:
                return [dic[n]+1,i+1]
