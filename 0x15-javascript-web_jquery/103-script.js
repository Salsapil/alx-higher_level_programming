$(document).ready(function() {
    const languageInput = $('#language_code');
  
    function fetch() {
      const languageCode = languageInput.val().trim();
      if (!languageCode) {
        alert('Please enter a language code.');
        return;
      }
  
      const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
  
      $('#hello').text('Loading...');

      $.getJSON(url, function(data) {
        const hello = data.hello;
  
        $('#hello').text(hello);
      })
    }
  
    $('#btn_translate').click(fetch);
  
  });
