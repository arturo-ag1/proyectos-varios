/*

    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.


*/

nums = [1,2,3,4]


function runningSum(nums){

    let totalSum = 0;
    for(let i = 0; i < nums.length; i++){
        totalSum = totalSum + nums[i];
        console.log(totalSum);
    }
}

runningSum(nums);
