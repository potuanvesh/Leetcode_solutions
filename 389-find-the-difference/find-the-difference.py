class Solution(object):
    def findTheDifference(self, s, t):
        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for i in t:
            if i in count:
                count[i] -= 1

                if count[i] < 0:
                    return i
            else:
                return i