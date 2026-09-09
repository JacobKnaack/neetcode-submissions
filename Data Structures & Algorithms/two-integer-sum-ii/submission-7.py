class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            compare = numbers[left] + numbers[right]
            if compare == target:
                return [left + 1, right + 1]
            elif compare > target:
                right -= 1
            else:
                left += 1

        return [1, 1]