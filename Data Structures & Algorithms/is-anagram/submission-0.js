class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const map = {};
        for (let i = 0; i < s.length; i++) {
            const char = s[i];
            if (map[char]) {
                map[char] = map[char] + 1;
            } else {
                map[char] = 1;
            }
        }
        for (let j = 0; j < t.length; j++) {
            const char = t[j];
            if (map[char]) {
                map[char] = map[char] - 1;
            } else {
                return false;
            }
        }
        const total = Object.values(map).reduce((acc, value) => acc + value, 0);
        return total === 0;
    }
}
