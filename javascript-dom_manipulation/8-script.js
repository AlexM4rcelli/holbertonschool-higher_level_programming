fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((res) => res.json())
  .then(({ hello }) => {
    document.getElementById('hello').textContent = hello;
  });