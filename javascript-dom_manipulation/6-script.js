fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    const newElement = document.createElement('p');
    newElement.innerHTML = `${data.name}`;
    document.querySelector('#character').appendChild(newElement)
  });