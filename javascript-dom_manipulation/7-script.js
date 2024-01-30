fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((res) => res.json())
  .then((data) => {
    const movies = data.results;
    const listMovies = document.querySelector('#list_movies');
    movies.forEach(movie => {
      const movieLi = document.createElement('li');
      movieLi.innerHTML= `${movie.title}`;
      listMovies.appendChild(movieLi);
    });
  });