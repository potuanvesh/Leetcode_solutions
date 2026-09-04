class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
      count=0
      maxi=0
      for i in nums:
        if i==1:
            count=count+1
            maxi=max(maxi,count)
        else:
            count=0
      return maxi