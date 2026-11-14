class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m=[]
        
        for i in range(len(accounts)):
            
            m.append(sum(accounts[i]))
            
        return max(m)
        