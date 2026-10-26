class Solution:
    def isHappy(self, n: int) -> bool:
        
        a=set()
        while n!=1:
            if n in a:
                return False
            a.add(n)
            total=0
            while n>0:
                digit=n%10
                total+=digit*digit
                n//=10
            n=total
        return True
        
        