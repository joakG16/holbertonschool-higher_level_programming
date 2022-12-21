/*
To toggle an element's class name whenever a user clicks on it using JavaScript,
you can use the classList property of the element and the toggle method.
*/

// Get the header element and the toggle_header element
const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

// Add a click event listener to the toggle_header element
toggleHeader.addEventListener('click', function () {
  // Toggle the "red" and "green" classes on the header element
  header.classList.toggle('red');
  header.classList.toggle('green');
});
