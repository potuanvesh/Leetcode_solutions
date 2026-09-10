class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        if n>=1000:
            count+=n-999
        if n>=1000000:
            count+=n-9999
        if n>=1000000000:
            count+=99999999
        return count
        