class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        d = {}
        max_occur = float('-inf')
        res = 0
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            max_occur = max(max_occur,d[s[right]])
            while ((right-left)+1)-max_occur>k:
                d[s[left]]-=1
                left+=1
            res = max(res,(right-left)+1)
        return res
            