const movieList = document.querySelector('#list_movies');

function addMovieToList (title) { // title = movie.title
  const newMovieNode = document.createElement('li');
  newMovieNode.innerText = title;
  movieList.append(newMovieNode);
}

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(resp => resp.json())
  .then(data => {
    for (const movie of data.results) {
      addMovieToList(movie.title);
    }
  });
