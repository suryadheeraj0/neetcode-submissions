class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        l = []
        d = Counter(nums)
        for i in d:
            bucket[d[i]].append(i)
        for i in range(len(bucket)-1,-1,-1):
            if len(bucket[i])>0:
                for j in bucket[i]:
                    l.append(j)
                    k-=1
                    if k==0:
                        break
            if k==0:
                break
        return l

        

        

