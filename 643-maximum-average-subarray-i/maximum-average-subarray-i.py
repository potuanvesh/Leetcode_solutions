class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum=0
        left=0
        ans=float('-inf')
        for right in range(len(nums)):
            sum+=nums[right]
            if right-left+1==k:
                ans=max(ans,float(sum)/k)
                sum-=nums[left]
                left+=1
                
        return ans
        