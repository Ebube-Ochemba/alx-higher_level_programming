/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
