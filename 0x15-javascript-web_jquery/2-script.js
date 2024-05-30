$(document).ready(function() {
  const readheader = $('#red_header');
  readheader.click(function() {
    const header = $('header');
    header.css('color', '#FF0000');
  });
});
