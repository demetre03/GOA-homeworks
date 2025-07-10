const countParagraph = document.getElementById("countParagraph");
const increaseBtn = document.getElementById("increaseBtn");

let count = 0;

increaseBtn.addEventListener("click", function() {
  count++;
  countParagraph.textContent = "Count: " + count;
});
