// n = word bank length
// m = target length

// Brute Force
// Time Complexity = O((n^m) * m)
// Space Complexity = O(m * m)  // because of slice
const canConstruct = (target, arr) => {
  // Base Case
  if (target === "") return true;

  for (let word of arr) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      if (canConstruct(suffix, arr)) {
        return true;
      }
    }
  }
  return false;
};

// Memoization
// Time Complexity = O(n * m^2)
// Space Complexity = O(m^2)
const canConstructMemo = (target, arr, memo = {}) => {
  if (target in memo) return memo[target];
  // Base Case
  if (target === "") return true;

  for (let word of arr) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      if (canConstructMemo(suffix, arr)) {
        memo[target] = true;
        return true;
      }
    }
  }

  memo[target] = false;
  return false;
};

// Test Cases
console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); // true
console.log(
  canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
); // false

console.log("\nMemoization:");
console.log(canConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcd"])); // true
console.log(
  canConstructMemo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
);
console.log(
  canConstructMemo("eeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eeee",
    "eeeeee",
    "eeeeeee",
  ])
); // false
console.log(
  canConstructMemo("eeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eeee",
    "eeeeee",
    "eeeeeee",
    "f",
  ])
); // true
