class Solution:
    def removeDuplicates(self, s: str) -> str:
        si=[]
        for i in s:
            if not si or si[-1]!=i:
                si.append(i)
            else:
                si.pop()
        return "".join(si)
        