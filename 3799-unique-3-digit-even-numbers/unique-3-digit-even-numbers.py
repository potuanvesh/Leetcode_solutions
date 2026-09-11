class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        from itertools import permutations
        d=set()
        for a,b,c in permutations(digits,3):
            if a!=0 and c%2==0:
                d.add(100*a+10*b+c)
        return len(d)

        