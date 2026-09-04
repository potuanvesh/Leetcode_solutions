class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        a=len(nums)
        return nums[a//2]
        