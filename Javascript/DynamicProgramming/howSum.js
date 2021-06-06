// Target Sum - Array Values - Can repeat same elements from array
//     Input (7, [5, 3, 4, 7])
//     Output 3, 4

//     Input (7, [2, 4])
//     Output null

// m = target
// n = array length

// Brute Force
// Time Complexity = O((n^m) * m)  // multiply by m because of copying of elements // exponential
// Space Complexity = O(m)
const howSum = (target, arr) => {
  // Base Case
  if (target === 0) return [];
  if (target < 0) return null;

  for (let num of arr) {
    const remainder = target - num;
    const result = howSum(remainder, arr);
    if (result !== null) {
      return [...result, num];
    }
  }
  return null;
};

// Memoization
// Time Complexity = O(n * m^2) // because of multiply by m because of copying in return
// Space Complexity = O(m^2)
const howSumMemo = (target, arr, memo = {}) => {
  if (target in memo) return memo[target];

  // Base case
  if (target === 0) return [];
  if (target < 0) return null;

  for (let num of arr) {
    const remainder = target - num;
    const result = howSumMemo(remainder, arr, memo);
    if (result !== null) {
      memo[target] = [...result, num];
      return memo[target];
    }
  }

  memo[target] = null;
  return null;
};

// console.log(howSum(7, [2, 3]));
// console.log(howSum(7, [5, 3, 4, 7]));
// console.log(howSum(7, [2, 4]));
// console.log(howSum(8, [2, 3, 5]));
// console.log(howSum(8, [3, 5, 2]));
// console.log(canSum(300, [7, 14]));  // Taking so much time

console.log("Memoize Solution");
console.log(howSumMemo(7, [2, 3]));
console.log(howSumMemo(7, [5, 3, 4, 7]));
console.log(howSumMemo(7, [2, 4]));
console.log(howSumMemo(7, [2, 4, 1]));
console.log(howSumMemo(8, [2, 3, 5]));
console.log(howSumMemo(300, [7, 14]));
