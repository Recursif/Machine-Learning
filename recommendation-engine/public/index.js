var data;

function preload() {
  data = loadJSON('movies.json');
}

function setup() {
  noCanvas();
  var users = {};
  var dropdown1 = createSelect('');
  var dropdown2 = createSelect('');
  for (var i = 0; i < data.users.length; i++) {
    var name = data.users[i].name;
    dropdown1.option(name);
    dropdown2.option(name);
    users[name] = data.users[i];
  }
  console.log(data);
  console.log(users);
  var button = createButton('submit');
  button.mousePressed(euclideanSimilarity);
  console.log(data);
}
