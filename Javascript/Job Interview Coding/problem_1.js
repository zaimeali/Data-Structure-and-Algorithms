// ([1, 3, 1, 4, 23], 8) return true because (3 + 1 + 4 = 8)
// ([1, 3, 1, 4, 23], 7) return false
// ([1, 3, 1, 4, 23], 27) return true because (4 + 23 = 27)
// ([1, 3, 1, 4, 23], 23) return true because (23 = 23)

const seqSum = (arr, res) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === res) {
      return true;
    }
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      sum += arr[j];
      if (sum === res) {
        return true;
      }
      if (sum > res) {
        break;
      }
    }
  }
  return false;
};

console.log(seqSum([1, 3, 1, 4, 23], 23));
console.log(seqSum([1, 3, 1, 4, 23], 27));
console.log(seqSum([1, 3, 1, 4, 23], 8));
console.log(seqSum([1, 3, 1, 4, 23], 7));
