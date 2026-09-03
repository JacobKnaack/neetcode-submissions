class Solution:

    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0
        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                floor = stack.pop()
                if len(stack) == 0:
                    break
                left = stack[-1]
                bounded_height = min(height[left], height[i]) - height[floor]
                width = i - left - 1
                total += bounded_height * width
            stack.append(i)
        return total