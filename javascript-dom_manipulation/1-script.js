const header = document.querySelector('#red_header');

header.addEventListener('click', (e) => {
  e.preventDefault();
  header.style.color = '#FF0000';
});