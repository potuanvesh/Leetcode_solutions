class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a=max(nums)
        b=min(nums)
        while b!=0:
            a,b = b ,a%b
        return a
        