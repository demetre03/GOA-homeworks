const paragraph = document.getElementById("myParagraph");
const bgColorBtn = document.getElementById("bgColorBtn");
const textColorBtn = document.getElementById("textColorBtn");
const fontSizeBtn = document.getElementById("fontSizeBtn");

bgColorBtn.addEventListener("click", function() {
  paragraph.style.backgroundColor = "lightblue";
});

textColorBtn.addEventListener("click", function() {
  paragraph.style.color = "red";
});

fontSizeBtn.addEventListener("click", function() {
  paragraph.style.fontSize = "24px";
});
