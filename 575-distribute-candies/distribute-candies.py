class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        count={}
        n=len(candyType)
        for i in candyType:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        if len(count)>=n//2:
            return n//2
        else:
            return len(count)