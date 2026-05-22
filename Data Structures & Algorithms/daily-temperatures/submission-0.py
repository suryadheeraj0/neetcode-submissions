class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                curr_ind = stack.pop()
                res[curr_ind] = (i-curr_ind)
            stack.append(i)
        return res