class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = []
        if len(nums)==0:
            return 0
        for i in nums:
            if i not in num:
                num.append(i)
        num = sorted(num)
        if len(num)==1:
            return 1
        res=[]
        count=1
        maxc = 0
        temp = []
        ptr = 0
        # print(num)
        while ptr <len(num)-1:
            if num[ptr+1]==num[ptr]+1:
                temp.append(num[ptr])
                count += 1
                if ptr == len(num)-2:
                    temp.append(num[ptr+1])
                    count += 1
            else:
                # print("else")
                # print(count)
                if count>1:
                    temp.append(num[ptr+1])
                    count+=1
                    if count > maxc:
                        maxc = count
                        res = temp
                
                count = 1
                temp = []
            ptr += 1
            if len(temp)>len(res):
                res = temp
        if len(res)==0:
            return 1
        return len(res)