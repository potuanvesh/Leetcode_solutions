class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sorted=[]
        a=max(nums)
        b=min(nums)
        for i in range(b,a+1):
            if i not in nums:
                sorted.append(i)
        return sorted
        