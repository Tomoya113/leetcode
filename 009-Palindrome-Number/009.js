/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const s = x.toString()
    return s.split('').reverse().join('') === s
};