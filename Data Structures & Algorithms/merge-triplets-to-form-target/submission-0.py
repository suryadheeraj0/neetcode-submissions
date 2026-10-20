class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False
        for i,j,k in triplets:
            if i>target[0] or j>target[1] or k>target[2]:
                continue
            if i==target[0]:
                first = True
            if j==target[1]:
                second = True
            if k==target[2]:
                third = True
        return first and second and third