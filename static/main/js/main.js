const navLinks = document.querySelector('.navLinks');
const closeMenu = document.getElementById('closeMenu');
const openMenu = document.getElementById('openMenu');

openMenu.addEventListener('click', open);
closeMenu.addEventListener('click', close);


function open(){
    navLinks.style.display = 'flex';
    openMenu.style.display = 'none';
    closeMenu.style.display = 'flex';
}

function close(){
    navLinks.style.display = '';
    openMenu.style.display = 'flex';
    closeMenu.style.display = 'none';
}