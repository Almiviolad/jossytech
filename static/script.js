const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
hamburger.addEventListener("click", function () {
  navLinks.classList.toggle("active");
  console.log(navLinks);
  hamburger.classList.toggle("toggle");
});

lucide.createIcons();
const swiper = new Swiper(".swiper", {
  direction: "horizontal",
  loop: true,
  centeredSlides: true,
  autoplay: true,
  breakpoints: {
    0: {
      slidesPerView: "auto",
    },
    768: {
      slidesPerView: 3,
      gap: 10,
    },
  },
});

document.querySelectorAll(".nav-links a").forEach((link) =>
  link.addEventListener("click", function () {
    navLinks.classList.remove("active");
  })
);
