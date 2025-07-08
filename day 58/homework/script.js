let score = 87; // შეგიძლია შეცვალო ნებისმიერ რიცხვზე 0-100 შუალედში

if (score < 0 || score > 100) {
  console.log("Invalid Score");
} else if (score === 100) {
  console.log("A+");
} else if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else if (score >= 70) {
  console.log("C");
} else if (score >= 60) {
  console.log("D");
} else if (score >= 40) {
  console.log("E");
} else {
  console.log("F");
}
