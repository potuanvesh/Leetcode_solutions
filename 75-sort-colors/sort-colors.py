class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0

        for x in nums:
            if x == 0:
                a += 1
            elif x == 1:
                b += 1
            else:
                c += 1

        i = 0

        while a > 0:
            nums[i] = 0
            i += 1
            a -= 1

        while b > 0:
            nums[i] = 1
            i += 1
            b -= 1

        while c > 0:
            nums[i] = 2
            i += 1
            c -= 1

        