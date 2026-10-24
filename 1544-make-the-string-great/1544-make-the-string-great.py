class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if not stack or stack[-1]!=i.swapcase():
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
        