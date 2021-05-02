// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/pairwise

const pairwise = (arr, arg) => {
  const unique = new Array();
  arr.forEach((item, index) => {
    for (let j = index + 1; j < arr.length; j++) {
      let sum = item + arr[j];
      if (sum === arg) {
        if (!unique.includes([index, j])) {
          unique.push([index, j]);
        }
      }
    }
  });

  const x = new Array();
  const y = new Array();
  let sum = 0;
  unique.forEach((item) => {
    if (
      !x.includes(item[0]) &&
      !y.includes(item[1]) &&
      !x.includes(item[1]) &&
      !y.includes(item[0])
    ) {
      x.push(item[0]);
      y.push(item[1]);
      sum += item[0] + item[1];
    }
  });
  console.log(sum);
};

pairwise([1, 4, 2, 3, 0, 5], 7);
pairwise([1, 3, 2, 4], 4);
pairwise([1, 1, 1], 2);
pairwise([0, 0, 0, 0, 1, 1], 1);
pairwise([], 100);
