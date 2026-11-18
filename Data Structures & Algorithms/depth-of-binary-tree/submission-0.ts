/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root: TreeNode | null): number {
        const countLevels = (node: TreeNode, count: number) => {
            if (!node) {
                return count;
            }
            return Math.max(countLevels(node.left, count + 1), countLevels(node.right, count + 1))
        }
        return countLevels(root, 0);
    }
}
