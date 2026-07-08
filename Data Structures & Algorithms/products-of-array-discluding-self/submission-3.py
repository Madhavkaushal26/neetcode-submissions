class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        bef = [1]*len(nums)
        aft = [1]*len(nums)
        for i in range(len(nums)):
            if i==0:
                bef[i] = nums[i]
                continue 
            bef[i] = bef[i-1]*nums[i]
        
        for i in range(len(nums)-1,0,-1):
            if i==len(nums)-1:
                aft[i] = nums[i]
                continue 
            aft[i] = aft[i+1]*nums[i]
     
        ptr = 0
        while ptr<len(nums):
            if ptr == 0:
                res.append(aft[ptr+1])
                ptr+=1
                continue
            if ptr == len(nums)-1:
                res.append(bef[ptr-1])
                ptr+=1
                continue
            tot = bef[ptr-1]*aft[ptr+1]
            res.append(tot)
            ptr+=1
        
        return res
        