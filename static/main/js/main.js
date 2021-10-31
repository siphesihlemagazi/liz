const mainMenu = document.querySelector('.mainMenu');
const closeMenu = document.querySelector('.closeMenu');
const openMenu = document.querySelector('.openMenu');
const navLinks = document.getElementById("menuLink").querySelectorAll("li");
var bars = document.getElementById("bars");


openMenu.addEventListener('click',show);
closeMenu.addEventListener('click',close);
// To make the nav close when a nav link is clicked
for (let i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click',close);
  }

function show(){
    mainMenu.style.display = 'flex';
    mainMenu.style.top = '0';
    bars.style.display = "none";
}
function close(){
    mainMenu.style.top = '-300%';
    bars.style.display = "block";
}


// Active nav link

let menuLinks = document.getElementById('menuLink').querySelectorAll('a');
menuLinks.forEach(a => {
    a.addEventListener('click', function () {
        menuLinks.forEach(link => link.classList.remove('active'));
        this.classList.add('active')
    })
})


//  Active pagination link

let paginations = document.getElementById('pagination').querySelectorAll('a');
paginations.forEach(a => {
    a.addEventListener('click', function () {
        paginations.forEach(link => link.classList.remove('active-pagination'));
        this.classList.add('active-pagination')
    })
})
