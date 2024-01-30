const addButton = document.querySelector('#add_item');
addButton.addEventListener('click', (e) => {
  e.preventDefault();
  const list = document.querySelector('.my_list');
  const newElement = document.createElement('li');
  newElement.innerHTML = 'Item';
  list.appendChild(newElement);
});