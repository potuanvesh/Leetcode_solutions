class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for i in strs:
            sorted_string=''.join(sorted(i))
            if sorted_string in hashmap:
                hashmap[sorted_string].append(i)
            else:
                hashmap[sorted_string]=[i]
        return hashmap.values()

        