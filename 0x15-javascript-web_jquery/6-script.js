$(document).ready(function () {
  const updateheader = $('#update_header');
  updateheader.click(function () {
    const header = $('header');
    header.text('New Header!!!');
  });
});
