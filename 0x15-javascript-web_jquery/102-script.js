document.addEventListener('DOMContentLoaded', () => {
  const container = $('#hello');
  const input = $('#language_code');
  const btn = $('#btn_translate');

  btn.on('click', () => {
    const value = input.val();
    const url = `https://fourtonfish.com/hellosalut/?lang=${value}`;

    $.getJSON(url, function () {
      console.log('success');
    })
      .done(function (data) {
        container.text(`${data.hello}`);
      })
      .fail(function () {
        console.log('error');
      });
  });
});
