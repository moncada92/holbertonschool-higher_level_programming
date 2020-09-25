document.addEventListener('DOMContentLoaded', () => {
  const container = $('#character');
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  $.getJSON(url, function () {
    console.log('success');
  })
    .done(function (data) {
      container.text(data.name);
    })
    .fail(function () {
      console.log('error');
    });
});
