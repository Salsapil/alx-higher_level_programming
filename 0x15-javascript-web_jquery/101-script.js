$(document).ready(function() {
  const list = $('.my_list');

  $('#add_item').click(function() {
    const newItem = $('<li>Item</li>');
    list.append(newItem);
  });

  $('#remove_item').click(function() {
    if (list.children().length > 0) {
      list.children().last().remove();
    }
  });

  $('#clear_list').click(function() {
    list.empty();
  });
});
