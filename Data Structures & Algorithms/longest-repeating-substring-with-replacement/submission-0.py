class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        length_char = 0
        res = 0
        left = 0
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            length_char = max(length_char,d[s[right]])
            if (right-left+1)<=length_char+k:
                res = max(res, (right-left)+1)
            else:
                d[s[left]]-=1
                left+=1
        return res