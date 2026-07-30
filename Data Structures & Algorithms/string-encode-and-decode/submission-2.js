class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (!strs.length) return 'void';
        const encoded = strs.map((string) => Buffer.from(string, 'utf-8').toString('base64'));
        const stringified = encoded.join(' ');
        return stringified;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if (str === 'void') return [];
        const encoded = str.split(' ');
        const stringified = encoded.map((string) => Buffer.from(string, 'base64').toString('utf-8'));
        return stringified;
    }
}
