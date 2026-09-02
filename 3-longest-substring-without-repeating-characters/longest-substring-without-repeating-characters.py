class Solution(object):
    def lengthOfLongestSubstring(self, s):
     unique=set()
     start=0
     max_len=0
     for end in range(len(s)):
        while s[end] in unique:
            unique.remove(s[start])
            start=start+1
        unique.add(s[end])
        length=end-start+1
        max_len=max(max_len,length)
     return max_len
