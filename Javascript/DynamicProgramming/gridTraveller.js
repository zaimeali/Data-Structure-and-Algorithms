// 2D Grid - Start to End - Can move Down and Right
// Tell how many ways to travel

// Brute Force
// Time Complexity = O(2^(m + n))
// Space Complexity = O(m + n)
const gridTraveller = (m, n) => {
  // Base case
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0) return 0;

  // (m-1) => down, (n-1) => right
  return gridTraveller(m - 1, n) + gridTraveller(m, n - 1);
};

// Memoization
// Time Complexity = O(m * n)
// Space Complexity = O(m + n)
const gridTravellerMemo = (m, n, memo = {}) => {
  const key = `${m},${n}`;
  if (key in memo) return memo[key];

  // Base Case
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0) return 0;

  memo[key] =
    gridTravellerMemo(m - 1, n, memo) + gridTravellerMemo(m, n - 1, memo);
  return memo[key];
};

// Tabulation
// Time Complexity = O(m * n)
// Space Complexity = O(m * n)
const gridTravellerTab = (m, n) => {
  const table = new Array(m + 1).fill().map(() => new Array(n + 1).fill(0));

  // Base Case
  table[1][1] = 1;

  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      const current = table[i][j];
      if (j + 1 <= n) table[i][j + 1] += current;
      if (i + 1 <= m) table[i + 1][j] += current;
    }
  }

  if (m < 5 && n < 5) {
    console.table(table);
  }
  return table[m][n];
};

// Test Cases

// // Brute Force
// console.log(gridTraveller(2, 3));
// console.log(gridTraveller(3, 3));
// // console.log(gridTraveller(18, 18));  // Taking so much time

// // Memoization
// console.log(gridTravellerMemo(2, 3));
// console.log(gridTravellerMemo(3, 3));
// console.log(gridTravellerMemo(18, 18));

// Tabulation
console.log(gridTravellerTab(2, 3));
console.log(gridTravellerTab(3, 3));
console.log(gridTravellerTab(18, 18));
