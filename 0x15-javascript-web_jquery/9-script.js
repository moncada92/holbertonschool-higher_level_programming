document.addEventListener('DOMContentLoaded', () => {
  const container = $('#hello');
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  $.getJSON(url, function () {
    console.log('success');
  })
    .done(function (data) {
      container.text(`Say ${data.hello}`);
    })
    .fail(function () {
      console.log('error');
    });
});
