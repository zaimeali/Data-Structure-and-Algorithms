const insertionSort = (arr) => {
  for (let k = 0; k < arr.length; k++) {
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
      }
    }
  }
  console.log(arr);
};

// insertionSort([1, 4, 2, 8, 345, 123]);
insertionSort([7, 4, 2, 8, 345, 1, 123]);
