$(document).ready(function() {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.getJSON(url, function(data) {
    const movieList = $('#list_movies');
      data.results.forEach(function(movie) {
      const movieListItem = $('<li>' + movie.title + '</li>');
      movieList.append(movieListItem);
    });
  });
});
