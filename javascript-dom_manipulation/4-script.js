const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addItemButton.addEventListener('click', function () {
  const newItem = document.createElement('li');
  // Set the text content of the new li element
  // to 'Item' using the textContent property.
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
