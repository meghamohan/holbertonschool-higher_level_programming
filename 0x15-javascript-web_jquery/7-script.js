const url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data) {
  $('div#character').text(data.name);
});
