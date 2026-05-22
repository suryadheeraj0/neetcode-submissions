class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d = Counter(s1)
        left = 0
        d1 = Counter()
        for right in range(len(s2)):
            d1[s2[right]]+=1
            if(right-left)+1>len(s1):
                d1[s2[left]]-=1
                if d1[s2[left]]==0:
                    del d1[s2[left]]
                left+=1
            if d == d1:
                return True
        return False