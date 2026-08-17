class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_freq = [0]*26
        t_freq = [0]*26
        for i in s:
            s_freq[ord(i)-ord('a')]+=1
        for j in t:
            t_freq[ord(j)-ord('a')]+=1
        for k in range(len(s_freq)):
            if s_freq[k]!=t_freq[k]:
                return False
        return True