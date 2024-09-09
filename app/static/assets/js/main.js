(function(){
   
const nav_div = document.querySelector('.mobile-nav-toggle')
nav_div.addEventListener('click', function(e) {
  const nav_bar = document.querySelector('#navbar')
  nav_bar.classList.toggle('navbar-mobile')
  this.classList.toggle('bi-list')
  this.classList.toggle('bi-x')
})


nav_drop_down = document.querySelector('.navbar .dropdown > a')
nav_drop_down.addEventListener('click', function(e) {
  if (document.querySelector('#navbar').classList.contains('navbar-mobile')) {
    e.preventDefault()
    this.nextElementSibling.classList.toggle('dropdown-active')
  }
}, true)  


})()












