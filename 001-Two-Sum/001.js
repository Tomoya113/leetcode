/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
let result = []


for(let i=0; i<nums.length; i++) {
    result[0] = i
    for(let i=0; i<nums.length; i++) {
        if (target - nums[result[0]] == nums[i] ) {
            result[1] = i
            break;
        }
    }
    if (result.length == 2) {break;}
}
return result;
};