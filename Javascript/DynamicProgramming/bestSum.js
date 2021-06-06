// Same like how sum problem but return the shortest combination
// bestSum(8, [2, 3, 5])
// not return [2, 2, 2, 2]
// not return [2, 3, 3]
// should return [3, 5]

// Brute Force
// Time Complexity = O((n^m) * m)  // multiply by m because of copying of elements // exponential
// Space Complexity = O(m^2)  // because of shortest combination storing
const bestSum = (target, arr) => {
  // Best Case
  if (target === 0) return [];
  if (target < 0) return null;

  let shortestCombination = null;

  for (let num of arr) {
    const remainder = target - num;
    const remainderCombo = bestSum(remainder, arr);
    if (remainderCombo) {
      const combination = [...remainderCombo, num];
      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination;
      }
    }
  }

  return shortestCombination;
};

// Memoization
// Time Complexity = O(n * m^2)  // multiply by m because of copying of elements // exponential
// Space Complexity = O(m^2) // because of shortest combination storing
const bestSumMemo = (target, arr, memo = {}) => {
  if (target in memo) return memo[target];

  // Best Case
  if (target === 0) return [];
  if (target < 0) return null;

  let shortestCombination = null;

  for (let num of arr) {
    const remainder = target - num;
    const remainderCombo = bestSumMemo(remainder, arr, memo);
    if (remainderCombo) {
      const combination = [...remainderCombo, num];
      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination;
      }
    }
  }

  memo[target] = shortestCombination;
  return shortestCombination;
};

console.log(bestSum(7, [2, 3]));
console.log(bestSum(8, [2, 3, 5]));

console.log(bestSumMemo(7, [2, 3]));
console.log(bestSumMemo(8, [2, 3, 5]));
console.log(bestSumMemo(100, [2, 3, 5, 25]));
