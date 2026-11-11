class Solution {
    static createTargetMap(t: string) {
        const map = new Map();
        for (const target of t) {
            map.has(target) ? map.set(target, map.get(target) + 1) : map.set(target, 1);
        }
        return map;
    }
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s: string, t: string): string {
        if (s.length === 0 || t.length === 0) return "";

        const targetMap = new Map<string, number>();
        for (const char of t) {
            targetMap.set(char, (targetMap.get(char) || 0) + 1);
        }

        const required = targetMap.size;
        let formed = 0;
        const windowCounts = new Map<string, number>();

        // storing the windowLength, left and right indices
        let ans = [-1, 0, 0];
        let l = 0;
        for (let r = 0; r < s.length; r++) {
            const char = s[r];
            windowCounts.set(char, (windowCounts.get(char) || 0) + 1);

            if (targetMap.has(char) && windowCounts.get(char) === targetMap.get(char)) {
            formed++;
            }
            while (l <= r && formed === required) {
            const leftChar = s[l];
            if (ans[0] === -1 || r - l + 1 < ans[0]) {
                ans[0] = r - l + 1;
                ans[1] = l;
                ans[2] = r;
            }
            windowCounts.set(leftChar, windowCounts.get(leftChar)! -1);
            if (targetMap.has(leftChar) && windowCounts.get(leftChar)! < targetMap.get(leftChar)!) {
                formed--;
            }
            l++;
            }
        }
        return ans[0] === -1 ? "" : s.substring(ans[1], ans[2] + 1);
    }
}
