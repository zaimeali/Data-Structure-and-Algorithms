// Target Sum - Array Values - Can repeat same elements from array
//     Input (7, [5, 3, 4, 7])
//     Output true because 3 + 4, 7

//     Input (7, [2, 4])
//     Output false

// m = target
// n = array length

// Brute Force
// Time Complexity = O(n^m)
// Space Complexity = O(m)
const canSum = (target, arr) => {
  // Base Case
  if (target === 0) return true;
  if (target < 0) return false;

  for (let num of arr) {
    const remainder = target - num;
    if (canSum(remainder, arr)) {
      return true;
    }
  }

  return false;
};

// Memoization
// Time Complexity = O(m * n)
// Space Complexity = O(m)
const canSumMemo = (target, arr, memo = {}) => {
  if (target in memo) return memo[target];

  // Base Case
  if (target === 0) return true;
  if (target < 0) return false;

  for (let num of arr) {
    const remainder = target - num;
    if (canSumMemo(remainder, arr, memo)) {
      memo[target] = true;
      return true;
    }
  }

  memo[target] = false;
  return false;
};

// Tabulation
// Time Complexity =
// Space Complexity =
const canSumTab = (target, arr) => {};

console.log("Brute Force Solution");
console.log(canSum(7, [2, 3]));
console.log(canSum(7, [5, 3, 4, 7]));
console.log(canSum(7, [2, 4]));
console.log(canSum(7, [2, 4, 1]));
console.log(canSum(8, [2, 3, 5]));
// console.log(canSum(300, [7, 14]));  // Taking so much time

console.log("\nMemoize Solution");
console.log(canSumMemo(7, [2, 3]));
console.log(canSumMemo(7, [5, 3, 4, 7]));
console.log(canSumMemo(7, [2, 4]));
console.log(canSumMemo(7, [2, 4, 1]));
console.log(canSumMemo(8, [2, 3, 5]));
console.log(canSumMemo(300, [7, 14]));

console.log("\nTabulation Solution");
console.log(canSumTab(7, [2, 3]));
console.log(canSumTab(7, [5, 3, 4, 7]));
console.log(canSumTab(7, [2, 4]));
console.log(canSumTab(7, [2, 4, 1]));
console.log(canSumTab(8, [2, 3, 5]));
console.log(canSumTab(300, [7, 14]));
