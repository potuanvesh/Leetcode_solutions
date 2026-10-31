class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        s = set()
        m=0
        d=0
        for i in range(len(nums)):
            if nums[i] in s:
                d = nums[i]
            else:
                s.add(nums[i])

        for i in range(1, len(nums) + 1):
           if i not in s:
            m = i
            break

        return [d, m]
        