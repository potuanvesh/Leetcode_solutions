class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares=[]
        for i in nums:
            squares.append(i*i)
        return sorted(squares)       