class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        res = []
        for i in strs:
            char_freq = [0]*26
            for j in i:
                char_freq[ord(j)-ord('a')]+=1
            d[str(char_freq)].append(i)
        for i in d:
            res.append(d[i])
        return res
            
