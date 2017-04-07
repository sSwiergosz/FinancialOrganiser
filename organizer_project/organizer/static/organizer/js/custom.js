$(".button-collapse").sideNav();


var elem = document.querySelector('.grid');

var pckry = new Packery( elem, {
  // options
  itemSelector: '.draggable',
  gutter: 10
});


// if you have multiple .draggable elements
// get all draggie elements
var draggableElems = document.querySelectorAll('.draggable');
// array of Draggabillies
var draggies = []
// init Draggabillies
for ( var i=0, len = draggableElems.length; i < len; i++ ) {
  var draggableElem = draggableElems[i];
  var draggie = new Draggabilly( draggableElem, {
    // options...
  });
  draggies.push( draggie );
}

