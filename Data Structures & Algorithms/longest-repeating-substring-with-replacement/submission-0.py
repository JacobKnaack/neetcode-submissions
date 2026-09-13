class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            max_frequency = max(max_frequency, counts[char])

            if (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length