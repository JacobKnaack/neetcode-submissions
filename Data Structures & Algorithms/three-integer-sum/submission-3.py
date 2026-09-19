class Solution:
    @staticmethod
    def bruteForce(nums: list[int]) -> List[List[int]]:
        triplets = set()
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                            triplets.add(triplet)
                            
        return [list(t) for t in triplets]

    @staticmethod
    def numsSorted(nums: List[int]) -> List[List[int]]:
        sorted = nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return triplets
 

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return Solution.bruteForce(nums)
        return Solution.numsSorted(nums)