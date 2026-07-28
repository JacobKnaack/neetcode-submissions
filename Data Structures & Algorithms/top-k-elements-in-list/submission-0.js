class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const counts = {};
        const results = [];
        for (let val of nums) {
            if (counts[val]) {
                counts[val] += 1;
            } else {
                counts[val] = 1;
            }
        }
        while (results.length < k) {
            let currentLargest = [null, 0];
            for (let [value, count] of Object.entries(counts)) {
                if (count > currentLargest[1]) {
                    currentLargest = [value, count];
                }
            }
            results.push(currentLargest[0]);
            delete counts[currentLargest[0]];
        }
        return results;
    }
}
