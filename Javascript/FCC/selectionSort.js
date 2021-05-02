const minValue = (arr) => {
  let min = arr[0];
  let minIndex = 0;
  arr.forEach((item, index) => {
    if (min > item) {
      min = item;
      minIndex = index;
    }
  });
  return {
    min,
    minIndex,
  };
};

const selectionSort = (arr) => {
  //   let x = 0;
  //   var { min, minIndex } = minValue(arr);
  //   let temp = arr[x];
  //   arr[x] = min;
  //   arr[minIndex] = temp;
  //   console.log(arr);
  //   x++;
  for (let i = 0; i < arr.length; i++) {
    let { min, minIndex } = minValue(arr.slice(i));
    let temp = arr[i];
    arr[i] = min;
    arr[minIndex + i] = temp;
  }
  console.log(arr);
};

// selectionSort([2, 4, 1, 5]);
selectionSort([1, 4, 2, 8, 345, 123]);
// selectionSort([7, 4, 2, 8, 345, 1, 123]);
//   selectionSort([
//     1,
//     4,
//     2,
//     8,
//     345,
//     123,
//     43,
//     32,
//     5643,
//     63,
//     123,
//     43,
//     2,
//     55,
//     1,
//     234,
//     92,
//   ]);
