class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_pos = {}
        max_pos = 0
        res = []
        left = 0
        for i in range(len(s)):
            char_pos[s[i]] = i
        for right in range(len(s)):
            max_pos = max(max_pos, char_pos[s[right]])
            if right==max_pos:
                res.append(right-left+1)
                left=right+1
        return res
