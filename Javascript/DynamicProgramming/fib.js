// Brute Force
// Time Complexity = O(2^n)
// Space Complexity = O(n)
const fib = (n) => {
  if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
};

// Memoization
// Time Complexity = O(n)
// Space Complexity = O(n)
const fibMemo = (n, memo = {}) => {
  if (n in memo) return memo[n];
  if (n <= 2) return 1;
  memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  return memo[n];
};

// Tabulation
// Time Complexity = O(n)
// Space Complexity = O(n)
const fibTab = (n) => {
  const table = new Array(n + 1).fill(0); // size of n and fill every value with 0
  table[1] = 1;
  for (let i = 0; i < n; i++) {
    table[i + 1] += table[i];
    table[i + 2] += table[i];
  }
  console.table(table);
  return table[n];
};

// Brute Force
console.log(fib(6));
// console.log(fib(50));  // taking so much time

// Memoization
console.log("\nMemoization");
console.log(fibMemo(6));
console.log(fibMemo(50));

// Tabulation
console.log("\nTabulation");
console.log(fibTab(6));
console.log(fibTab(50));
