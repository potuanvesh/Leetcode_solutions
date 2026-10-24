class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        b=[]
        for i in range(1,n+1):
            b.append("Push")
            if i not in target:
                b.append("Pop")
            if i == target[-1]:
                break
        return b
                


                
            

        