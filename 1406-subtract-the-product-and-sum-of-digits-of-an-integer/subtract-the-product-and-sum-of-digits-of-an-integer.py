class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        s=0
        while n>0:
            temp=n%10
            s=s+temp
            product=temp*product
            n=n//10
        return product-s


        