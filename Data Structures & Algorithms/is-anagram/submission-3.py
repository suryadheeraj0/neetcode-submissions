class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
           return False
       d = {}
       d1 = {}
       for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
       for j in t:
        if j in d1:
            d1[j]+=1
        else:
            d1[j]=1
       for i in d:
        if i not in d1:
            return False
        else:
            if d[i]!=d1[i]:
                return False
       return True
