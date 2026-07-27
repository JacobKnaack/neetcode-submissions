class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const isAnagram = (str1, str2) => {
            if (str1.length !== str2.length) return false;

            const letters1 = {};
            const letters2 = {};
            for (let i = 0; i < str1.length; i++) {
                let stringChar1 = str1[i];
                let stringChar2 = str2[i];
                if (letters2[stringChar2]) {
                    letters2[stringChar2] += 1;
                } else {
                    letters2[stringChar2] = 1;
                }
                if (letters1[stringChar1]) {
                    letters1[stringChar1] += 1;
                } else {
                    letters1[stringChar1] = 1;
                }
            }
            for (let key of Object.keys(letters1)) {
                if (letters1[key] !== letters2[key]) {
                    return false;
                }
            }
            return true
        }
        const matches = [];
        for (let current of strs) {
            let matched = false;
            // search matches for anagram
            for (let list of matches) {
                const listMatch = list[0];
                if (isAnagram(listMatch, current)) {
                    list.push(current);
                    matched = true;
                    break;
                }
            }
            if (!matched) {
                matches.push([current]);
            }
        }
        return matches;
    }
}
