var element1 = document.getElementById('element-1');
var element2 = document.getElementById('element-2');
var element3 = document.getElementById('element-3');

element3.onclick = function() {
	element1.classList.add('show');
};

element1.onclick = function(event) {
	if (event.target !== event.currentTarget) {
  	return;
  }
	element1.classList.remove('show');
};