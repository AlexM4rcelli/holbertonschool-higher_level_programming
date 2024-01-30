const header = document.querySelector('#red_header');

header.addEventListener('click', (e) => {
  e.preventDefault();
  header.classList.add('red');
});