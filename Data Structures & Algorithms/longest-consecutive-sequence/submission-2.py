class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums_dupes = sorted(nums)
        sorted_nums = list(dict.fromkeys(sorted_nums_dupes))
        consecutive = []
        max_consecutive = 0
        for num in sorted_nums:
            last_consecutive = None
            if len(consecutive) > 0:
                last_consecutive = consecutive[-1]
            else:
                consecutive.append(num)
            if last_consecutive is not None:
                if num == last_consecutive + 1:
                    consecutive.append(num)
                else:
                    consecutive = [num]
            max_consecutive = max(max_consecutive, len(consecutive))

        return max_consecutive
