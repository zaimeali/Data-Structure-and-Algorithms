// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update

function updateInventory(arr1, arr2) {
  for (let elem of arr2) {
    let index = arr1.findIndex((item) => item[1] === elem[1]);
    if (index >= 0) {
      arr1[index][0] += elem[0];
    } else {
      arr1.push(elem);
    }
  }
  arr1.sort(function (a, b) {
    return a[1] > b[1] ? 1 : -1;
  });
  return arr1;
}

// Example inventory lists
var curInv = [
  [21, "Bowling Ball"],
  [2, "Dirty Sock"],
  [1, "Hair Pin"],
  [5, "Microphone"],
];

var newInv = [
  [2, "Hair Pin"],
  [3, "Half-Eaten Apple"],
  [67, "Bowling Ball"],
  [7, "Toothpaste"],
];

updateInventory(curInv, newInv);
