const hamburger = document.getElementById("hamburger");
const nav = document.getElementById("navbar_");

hamburger.addEventListener('click', () => {
    nav.classList.toggle("show");
});