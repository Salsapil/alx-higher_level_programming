$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val().trim();
    if (!languageCode) {
      alert('Please enter a language code.');
      return;
    }

    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
    $.getJSON(url, function(data) {
      const hello = data.hello;
      $('#hello').text(hello);
    });
  });
});
