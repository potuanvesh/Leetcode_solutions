class Solution(object):

    def maxVowels(self, s, k):

        v = 'aeiou'
        count = 0
        left = 0
        ans = 0

        for right in range(len(s)):

            if s[right] in v:
                count += 1

            if right - left + 1 == k:
                ans = max(ans, count)

                if s[left] in v:
                    count -= 1

                left += 1

        return ans