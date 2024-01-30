const updateButton = document.querySelector('#update_header');

updateButton.addEventListener('click', (e) => {
  e.preventDefault();
  const header = document.querySelector('header');
  header.innerHTML = 'New Header!!!';
});