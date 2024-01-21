function getRandomHexColor() {
    return `#${Math.floor(Math.random() * 16777215).toString(16)}`;
  }
  
  const colorValue = document.querySelector('#text');
  const changeColorButton = document.querySelector('.test');
  
  changeColorButton.addEventListener('click', onClickChangeColorButton);
  
  function onClickChangeColorButton () {
    colorValue.style.color = getRandomHexColor();
    document.body.style.backgroundColor = getRandomHexColor();
  }
