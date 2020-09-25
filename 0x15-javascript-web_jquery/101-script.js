document.addEventListener('DOMContentLoaded', () => {
  const container = $('.my_list');
  $('#add_item').on('click', function () {
    const item = '<li>Item</li>';
    container.append(item);
  });
  $('#remove_item').on('click', function () {
    $('.my_list li').last().remove();
  });
  $('#clear_list').on('click', function () {
    container.empty();
  });
});
