class Solution(object):
    def strStr(self, haystack, needle):
        a,m=len(haystack),len(needle)
        for  i in range(a-m+1):
            if haystack[i:i+m]==needle[:]:
                return i
        return -1

       
        