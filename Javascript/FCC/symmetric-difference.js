// find-the-symmetric-difference
// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference

const sym = (args) => {
  let arr1 = new Set(arguments[0]);
  for (let i = 1; i < arguments.length; i++) {
    let arr2 = new Set(arguments[i]);
    for (let elem of arr2) {
      if (arr1.has(elem)) {
        arr1.delete(elem);
      } else {
        arr1.add(elem);
      }
    }
  }
  return Array.from(arr1).sort();
};

sym([1, 2, 3], [5, 2, 1, 4]);
