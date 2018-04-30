var data;

function preload() {
  data = loadJSON('movie.json');
}

function setup() {
  noCanvas();
  console.log(data);
}
