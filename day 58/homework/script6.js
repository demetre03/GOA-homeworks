let headsButton = document.getElementById("headsBtn");
let tailsButton = document.getElementById("tailsBtn");
let resultParagraph = document.getElementById("resultText");

headsButton.addEventListener("click", function () {
  resultParagraph.textContent = "Heads";
});

tailsButton.addEventListener("click", function () {
  resultParagraph.textContent = "Tails";
});
