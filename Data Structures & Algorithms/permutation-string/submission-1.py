from collections import Counter

class Solution:
    @staticmethod
    def compareChars(target: str, window: str) -> bool:
        return not (Counter(target) - Counter(window))
        

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        left = 0
        right = window_size
        result = False

        while right <= len(s2):
            chars = s2[left:right]
            result = Solution.compareChars(chars, s1)
            if result == True:
                break
            right += 1
            left += 1

        return result