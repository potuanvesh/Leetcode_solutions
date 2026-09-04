class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=[]
        
        for i in range(len(accounts)):
            
            m.append(sum(accounts[i]))
            
        return max(m)
        

        