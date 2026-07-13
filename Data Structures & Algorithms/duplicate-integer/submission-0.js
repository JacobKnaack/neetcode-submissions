class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const duplicates = new Set();
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            if (duplicates.has(num)) {
                return true;
            } else {
                duplicates.add(num);
            }
        }
        return false;
    }
}
