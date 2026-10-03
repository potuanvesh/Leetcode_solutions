class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count:
            if count[i]>1:
                a=i
        return a
        