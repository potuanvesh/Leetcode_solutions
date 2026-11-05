class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        a=[]
        for i in range(len(nums)):
            a.append(nums[i])
        count=0
        for i in a:
            digits=0
            while i>0:
                i//=10
                digits+=1
            if digits%2==0:
                count+=1
        return count



        