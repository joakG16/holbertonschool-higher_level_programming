const helloIdElem = document.getElementById('hello');

fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then(resp => resp.json())
  .then(data => {
    console.log(data);
    helloIdElem.innerText = data.hello;
  })
  .catch(err => console.log(err));
