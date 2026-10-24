class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=="[" or i=='{':
                stack.append(i)
            else:
                if not stack:
                    return False
                x=stack.pop()
                if x=='(' and i!=')':
                    return False
                elif x=='{'and i!='}':
                    return False
                elif x=='[' and i!=']':
                    return False
        return len(stack)==0
            
        
