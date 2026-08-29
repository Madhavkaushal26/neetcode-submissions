class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dl = [1]*len(nums)
        
        for i in range(1,len(nums)):
            subS = []
            for k in range(i):
                if nums[k]<nums[i]:
                    subS.append(dl[k])
            dl[i] = 1 + max(subS,default = 0)
        
        return max(dl)
        
        