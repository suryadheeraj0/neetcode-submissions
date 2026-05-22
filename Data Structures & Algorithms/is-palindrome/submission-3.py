class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:

            # Skip non-alphanumeric from left
            if not s[i].isalnum():
                i += 1

            # Skip non-alphanumeric from right
            elif not s[j].isalnum():
                j -= 1

            else:

                # Compare after lowercase
                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1

        return True