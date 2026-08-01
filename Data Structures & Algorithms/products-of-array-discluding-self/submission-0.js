class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const products = [];
        for (let i = 0; i < nums.length; i++) {
            let product = 1;
            for (let j = 0; j < nums.length; j++) {
                const num_j = nums[j];
                if (i !== j) {
                    product *= num_j;
                }
            }
            products.push(product);
        }
        return products;
    }
}
