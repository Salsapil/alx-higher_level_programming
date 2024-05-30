$(document).ready(function() {
  const toggleheader = $('#toggle_header');

  toggleheader.click(function() {
    const header = $('header');
    const currentClass = header.attr('class');

    if (currentClass === 'red') {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
  