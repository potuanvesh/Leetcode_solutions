class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=[]
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            
            m.append(sum)
        return m
        