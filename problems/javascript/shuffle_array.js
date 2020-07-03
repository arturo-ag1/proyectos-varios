/*

    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].


     x1, x2, x3, y1, y2, y3
    [ 2, 5,  1, 3, 4,  7]
*/

//Variables to run the program
let nums = [1,2,3,4,4,3,2,1]
let n = 4

/**
 * 
 * @param {number[]} nums 
 * @param {number} n 
 * @returns {number[]} numsSolved 
 */
function shuffleArray(nums,n){
    //Array to store the shuffled data
    let numsSolved = []

    
    //First step, we have to verify that n is exactly half the length of the array.
    let divider = nums.length / 2
    if(n != divider){
        console.log("Error, n has to be half the length of the array")
    }else{  
        //If it is, we will push the data to the new array, the concept is:
        //If there's half x and half y we push the first of each one, we can use the divider
        //variable to keep it simple.
        for(let i = 0; i < divider; i++){
            numsSolved.push(nums[i])
            numsSolved.push(nums[i+divider])
        }
        return numsSolved
    }
    
}


nums = shuffleArray(nums,n)

console.log(nums)