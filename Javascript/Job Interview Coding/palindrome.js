function palindrome(str) {
  str = str.toLowerCase();
  let str2 = str.split(""); // convert string into array
  str2.reverse(); // reverse array
  str2 = str2.join(""); // convert array into string
  if (str === str2) {
    console.log("It's Palindrome");
  } else {
    console.log("It's Not Palindrome");
  }
}

palindrome("Nice");
palindrome("lapPal");
