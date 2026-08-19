import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedLower = s.strip().lower()
        normalized = re.sub(r'[^a-zA-Z0-9]', '', strippedLower)
        for i in range(len(normalized)):
            char = normalized[i]
            end = normalized[(len(normalized) - i) - 1]
            if (char != end):
                return False
        return True

        