document.addEventListener('DOMContentLoaded', () => {
  const container = $('#hello');
  const input = $('#language_code');
  const btn = $('#btn_translate');

  function executeAjax (url) {
    $.getJSON(url, function () {
      console.log('success');
    })
      .done(function (data) {
        container.text(`${data.hello}`);
      })
      .fail(function () {
        console.log('error');
      });
  }

  btn.on('click', () => {
    const value = input.val();
    const url = `https://fourtonfish.com/hellosalut/?lang=${value}`;
    executeAjax(url);
  });

  input.focusin(() => {
    input.on('keypress', function (e) {
      const value = input.val();
      const url = `https://fourtonfish.com/hellosalut/?lang=${value}`;
      if (e.which === 13) {
        executeAjax(url);
      }
    });
  });
});
