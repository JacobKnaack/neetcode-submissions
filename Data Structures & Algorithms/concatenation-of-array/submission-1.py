import math

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums) * 2
        ans = [0] * size
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans
