class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = {};
        for (let i = 0; i < nums.length; i++) {
            const value = nums[i];
            const difference = target - value;
            if (value in map) {
                return [map[value], i];
            } else {
                map[difference] = i;
            }
        }
    }
}
