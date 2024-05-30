/* global $ */
$(document).ready(function () {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        $('#character').text(data.name);
      },
      error: function (xhr, status, error) {
        console.error('Error fetching character:', error);
      }
    });
  });
  