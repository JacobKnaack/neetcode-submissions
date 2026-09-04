import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def traverse(left: int, right: int) -> int | None:
            if left >= right:
                return None

            middle_index = math.floor((right + left) / 2)
            if nums[middle_index] == target:
                return middle_index

            if target < nums[middle_index]:
                return traverse(left, middle_index)
            if target > nums[middle_index]:
                return traverse(middle_index + 1, right)
        
        search_index = traverse(0, len(nums))
        if search_index is None:
            search_index = -1

        return search_index