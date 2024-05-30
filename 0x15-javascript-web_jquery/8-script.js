/* global $ */
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function (xhr, status, error) {
      console.error('Error fetching movies:', error);
    }
  });
});
