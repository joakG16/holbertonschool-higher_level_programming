function addClass () {
  // get reference to the header tag
  const redHeader = document.getElementById('red_header');
  // add the class
  redHeader.classList.add('red');
}
document.getElementById('red_header').addEventListener('click', addClass);
