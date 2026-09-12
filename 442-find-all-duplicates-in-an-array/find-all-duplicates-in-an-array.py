class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count={}
        n=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if count[i]>1:
                n.append(i)
        return n
            
        
        