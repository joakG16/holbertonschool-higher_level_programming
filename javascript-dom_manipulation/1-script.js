function changeColor () {
  // get reference to the header id element
  const redHeader = document.getElementById('red_header');
  // update the text color to red
  redHeader.style.color = '#ff0000';
}
//  attach a click event listener to the tag with id "red_header", and the respecitve function
document.getElementById('red_header').addEventListener('click', changeColor);
