class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26

        for i in s1:
            s1_freq[ord(i) - ord('a')] += 1

        s2_freq = [0] * 26

        left = 0
        right = 0

        while right < len(s2):
            index = ord(s2[right]) - ord('a')

            if s1_freq[index] == 0:
                s2_freq = [0] * 26
                left = right + 1
                right += 1

            else:
                s2_freq[index] += 1

                if s2_freq[index] > s1_freq[index]:
                    while s2_freq[index] > s1_freq[index]:
                        left_index = ord(s2[left]) - ord('a')
                        s2_freq[left_index] -= 1
                        left += 1

                # Check whether current window is a permutation
                if s2_freq == s1_freq:
                    return True

                right += 1

        return False