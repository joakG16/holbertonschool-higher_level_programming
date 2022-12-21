fetch('https://swapi-api.hbtn.io/api/people/5/?format=json') // This function returns a Promise that resolves to a Response object containing the response data.
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').innerHTML = data.name;
  })
  .catch(error => {
    console.error(error);
  });

/*
This script sends a request to the specified URL using the
fetch() function, parses the response data as JSON using
the .json() method, and then updates the content of the
element with the ID "elementId" using the innerHTML
property.
*/
