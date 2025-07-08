let movies = ["Inception", "Avatar", "Interstellar", "The Matrix"];
let favoriteMovie = "Interstellar";

let message = movies.includes(favoriteMovie)
  ? "The Film That You Chose Is In The List"
  : "The Film That You Chose Is Not In The List";

console.log(message);
