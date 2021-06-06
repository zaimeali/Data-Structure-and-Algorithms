function count(str) {
  str = str.toLowerCase();
  str = str.replace(/[^a-z]/g, "");
  let obj = {};

  for (let i = 0; i < str.length; i++) {
    let word = str[i];
    if (word in obj) {
      obj[word] += 1;
    } else {
      obj[word] = 1;
    }
  }

  return obj;
}

console.table(count("abacd"));
console.table(count("aba cd$ afakbra"));
