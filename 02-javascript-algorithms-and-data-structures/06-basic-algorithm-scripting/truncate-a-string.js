function truncateString(str, num) {
  // Clear out that junk in your trunk
  console.log(str, str.length, num);
  if (str.length <= num) {
    return str;
  } else {
    console.log(str.slice(0, num) + "...");
    return str.slice(0, num) + "...";
  }
}

truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length);
truncateString("A-tisket a-tasket A green and yellow basket", 8);
