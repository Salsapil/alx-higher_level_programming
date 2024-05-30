$(document).ready(function() {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.getJSON(url, function(data) {
    const hello = data.hello;
    const div = $('#hello');
    div.text(hello);
  });
});
