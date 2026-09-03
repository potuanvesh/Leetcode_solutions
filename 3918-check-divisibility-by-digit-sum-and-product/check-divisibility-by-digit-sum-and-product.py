class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp=n
        sum=0
        product=1
        while temp:
            digit=temp%10
            sum+=digit
            product*=digit
            temp=temp//10
        return n%(sum+product)==0
        