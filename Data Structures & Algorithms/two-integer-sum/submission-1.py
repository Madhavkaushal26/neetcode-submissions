class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dmap = {} #key = val , value = index
        
        for i,n in enumerate(nums):
            diff = target-n
            if diff in Dmap:
                return [Dmap[diff],i]
            Dmap[n]=i