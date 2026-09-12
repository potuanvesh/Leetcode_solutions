class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        a=len(nums)
        n=[]
        count={}
        for i in nums:
            if i in  count:
                count[i]+=1
            else:
                count[i]=1
            if count[i]>a/3 and i not in n:
                n.append(i)
        return n
                
        