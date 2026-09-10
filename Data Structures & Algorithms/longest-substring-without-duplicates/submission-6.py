class Solution:
    @staticmethod
    def naive(s: str) -> int:
        chars = set()
        largest = 0
        left = 0
        right = 0
        while left < len(s):
            while right < len(s):
                char = s[right]
                if char in chars:
                    count = len(chars)
                    if count > largest:
                        largest = count
                    chars = set()
                    break
                else:
                    chars.add(char)
                    right += 1
            left += 1
            right = left
        if len(chars) > largest:
            return len(chars)
        return largest

    @staticmethod
    def slidingWindow(s: str) -> int:
        chars = set()
        left = 0
        largest = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            largest = max(largest, right - left + 1)
        return largest


    def lengthOfLongestSubstring(self, s: str) -> int:
        return Solution.slidingWindow(s)