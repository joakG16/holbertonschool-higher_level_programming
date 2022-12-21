const updHeader = document.getElementById('update_header');
const header = document.querySelector('header');

updHeader.addEventListener('click', function () {
  // get or set the text content of the node or element.
  header.textContent = 'New header!!';
});
