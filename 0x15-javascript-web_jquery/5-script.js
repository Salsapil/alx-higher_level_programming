$(document).ready(function() {
  const addli = $('#add_item');
  addli.click(function() {
    const list = $('UL.my_list');
    const newitem = $('<li>Item</li>');
    list.append(newitem)
  });
});
