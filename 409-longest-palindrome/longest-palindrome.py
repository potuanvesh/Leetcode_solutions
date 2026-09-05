class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=set()
        ans=0
        for i in s:
            if i in count:
                count.remove(i)
                ans+=2
            else:
                count.add(i)

        if count:
            ans+=1
        return ans 

        