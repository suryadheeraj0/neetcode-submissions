class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unq_char = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in unq_char:
                unq_char.remove(s[left])
                left+=1
            unq_char.add(s[right])
            res = max(res,(right-left)+1)
        return res