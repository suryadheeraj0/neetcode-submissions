class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l = [[] for i in range(len(nums))]
        for i in d:
            l[d[i]-1].append(i)
        total_count = 0
        res = []
        for i in range(len(l)-1,-1,-1):
            if len(l[i])>=1:
                j = 0
                while j<len(l[i]) and total_count<k:
                    res.append(l[i][j])
                    j+=1
                    total_count+=1
                if total_count==k:
                    break
        return res