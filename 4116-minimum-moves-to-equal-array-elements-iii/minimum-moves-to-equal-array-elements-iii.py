class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        a=max(nums)
        for i in nums:
            while i!=a:
                i+=1
                count+=1
        return count
        