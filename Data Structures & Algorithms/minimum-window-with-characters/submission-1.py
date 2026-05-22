class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = Counter(t)
        left = 0
        d1 = {}
        res = ''
        min_window = float('inf')
        for right in range(len(s)):
            if s[right] in d:
                if s[right] in d1:
                    d1[s[right]]+=1
                else:
                    d1[s[right]]=1
            while self.check_dict(d,d1):
                if s[left] in d1:
                    d1[s[left]]-=1
                    if d1[s[left]]==0:
                        del d1[s[left]]
                if (right-left)+1<min_window:
                    min_window = (right-left)+1
                    res = s[left:right+1]
                left+=1
        return res
    def check_dict(self, d, d1):

        for i in d:

            if d1.get(i, 0) < d[i]:
                return False

        return True

