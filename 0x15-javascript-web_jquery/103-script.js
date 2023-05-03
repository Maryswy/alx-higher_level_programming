$(document).ready(function () {
  $('#btn_translate, #language_code').click(function () {
    translateHello();
  });

  ('#language_code').on('keyup', function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;

    $.getJSON(url, function (data) {
      ('#hello').html(data.hello);
    });
  }
});
