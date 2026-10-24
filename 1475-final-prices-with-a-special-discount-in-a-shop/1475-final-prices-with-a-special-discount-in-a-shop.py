class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack=[]
        ans=list(prices)
        for i in range(len(prices)):
            while stack and prices[i]<=prices[stack[-1]]:
                idx=stack.pop()
                ans[idx]-=prices[i]
            stack.append(i)
        return ans



        