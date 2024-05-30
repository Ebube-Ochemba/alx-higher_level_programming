/* global $ */
$(document).ready(function () {
  function fetchHello () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the Enter key code
      fetchHello();
    }
  });
});
