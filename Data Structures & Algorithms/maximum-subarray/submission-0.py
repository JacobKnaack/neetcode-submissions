class Solution:
    # O(n^2)
    def bruteForce(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(curSum, maxSum)
        return maxSum

    # Kadanes Algorithm
    # Instead of brute force addition of all numbers, we restart our
    # sum at zero when we now that adding previous sum will make our sum smaller.
    def kadanes(self, nums: List[int]) -> int:
        # Use 2 pointers
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            # ignore negative numbers, current sum resets at 0
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum     

    def maxSubArray(self, nums: List[int]) -> int:
        # return self.bruteForce(nums)
        return self.kadanes(nums)
