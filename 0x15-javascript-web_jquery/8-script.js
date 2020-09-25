document.addEventListener('DOMContentLoaded', () => {
  const container = $('#list_movies');
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  $.getJSON(url, function () {
    console.log('success');
  })
    .done(function (data) {
      $.each(data.results, function (key, values) {
        const textMovie = `<li>${values.title}</li>`;
        container.append(textMovie);
      });
    })
    .fail(function () {
      console.log('error');
    });
});
