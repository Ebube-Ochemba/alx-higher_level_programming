/* global $ */
$(document).ready(() => {
    $('INPUT#btn_translate').on('click', () => {
        const lang = $('INPUT#language_code').val();
        const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
        $.get(apiUrl, (data) => {
            $('DIV#hello').text(data.hello);
        });
    });
});
  