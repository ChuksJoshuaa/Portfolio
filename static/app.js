const toggleBtn = document.querySelector(".sidebar-toggle");
const closeBtn = document.querySelector(".come");
const Come = document.querySelectorAll(".coming");
const sidebar = document.querySelector(".sidebar");
const navBar = document.getElementById("nav")

toggleBtn.addEventListener("click", function () {
  sidebar.classList.toggle("show-sidebar");
});

closeBtn.addEventListener("click", function () {
  sidebar.classList.remove("show-sidebar");
});

Come.forEach(function (btn) {
   btn.addEventListener('focus', function () {
     const butt = document.querySelector(".sidebar");
    butt.classList.remove("show-sidebar")
   })
})


window.addEventListener('scroll', function() {
  const scrollHeight = window.pageYOffset;
  const navHeight = navBar.getBoundingClientRect().height;

  if(scrollHeight > navHeight) {
     navBar.classList.add("fixed-nav")
  }
  else {
    navBar.classList.remove("fixed-nav")
  }
})
