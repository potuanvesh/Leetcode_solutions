class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxi=0
        
        for i in sentences:
            count=0
            m=0
            n=len(i)
            while m<n:
                if not i[m].isalpha():
                    count+=1
                m+=1
            maxi=max(maxi,count)
        return maxi+1
        