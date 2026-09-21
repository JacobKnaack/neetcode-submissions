class Solution:
    @staticmethod
    def calculateArea(left: int, right: int, heights: List[int]) -> int:
        width = right - left
        height = min(heights[left], heights[right])
        return width * height

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = 0

        while left < right:
            area = Solution.calculateArea(left, right, heights)
            if area > max:
                max = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max
