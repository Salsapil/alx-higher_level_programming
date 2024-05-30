$(document).ready(function() {
    const readheader = $('#red_header');
    readheader.click(function() {
      const header = $('header');
      header.addClass('red');
    });
  });
