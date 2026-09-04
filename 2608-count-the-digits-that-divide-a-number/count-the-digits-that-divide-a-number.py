class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        temp=num
        while temp>0:
            digit=temp%10
            if num%digit==0:
                count+=1
           
            temp=temp//10
        return count
        