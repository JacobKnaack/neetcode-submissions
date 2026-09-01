class Solution:
    def kadanes(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Apply Kadanes algorithm, but remove the smallest value
        maxSum = nums[0]
        curSum = 0

        minSum = nums[0]
        curMin = 0

        total = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)

            curMin = min(curMin, 0)
            curMin += n
            minSum = min(minSum, curMin)

            total += n

        if maxSum < 0:
            # handles cases where all numbers are negative
            return maxSum

        return max(maxSum, total - minSum)
