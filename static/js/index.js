const BUTTON = document.querySelector('button')
// const BUTTON = document.getElementById('butt on')

const TOGGLE = () => {
  BUTTON.setAttribute(
    'aria-pressed',
    BUTTON.matches('[aria-pressed=true]') ? false : true
  )
}
window.onload=function(){BUTTON.addEventListener('click',TOGGLE)}
