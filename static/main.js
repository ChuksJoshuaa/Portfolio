const topLinks = document.querySelector(".top-link");

window.addEventListener('scroll', function() {
  const scrollHeight = window.pageYOffset;

  if(scrollHeight > 600) {
       topLinks.classList.add("show-link")
  }
  else {
      topLinks.classList.remove("show-link")
  }

})

const dateEl = document.getElementById("date")
now = new Date().getFullYear()
dateEl.innerHTML = now;
