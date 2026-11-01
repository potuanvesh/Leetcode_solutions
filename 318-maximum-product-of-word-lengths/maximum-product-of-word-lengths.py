class Solution:
    def maxProduct(self, words: list[str]) -> int:
        max_product=0
        a=[]
        for i in words:
            a.append(set(i))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if a[i].isdisjoint(a[j]):
                    product=len(words[i]) * len(words[j])
                    max_product=max(max_product,product)
        return max_product
        