class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count={}
        for i in arr1:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        result=[]
        for i in arr2:
            if i in count:
                for j in range(count[i]):
                    result.append(i)
                del count[i]   
        remaining=[]
        for i in count:
            for j in range(count[i]):
                remaining.append(i)
        remaining.sort() 
        result.extend(remaining) 
        return result   
        