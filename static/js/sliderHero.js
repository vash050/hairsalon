console.log("hh");
const breakpoint = window.matchMedia("(min-width:1200px)");
const breakpointMobilG = window.matchMedia("(max-width:544px)");
const breakpointTablet = window.matchMedia("(max-width:1000px)");
let swiperGallery, swiperProfi;

const enableSwiperGallery = function () {
  swiperGallery = new Swiper(".swiper-gallery", {
    grabCursor: true,
    effect: "coverflow",
    slidesPerView: "auto",
    centeredSlides: true,
    loop: true,

    coverflowEffect: {
      rotate: 0,
      stretch: 50,
      depth: 100,
      modifier: 2,
      scale: 1,
      slideShadows: false,
    },
  });
};

const enableSwiperGalleryMobile = function () {
  swiperGallery = new Swiper(".swiper-gallery", {
    loop: true,
    centeredSlides: true,
    slidesPerView: 1,
    slidesPerGroup: 1,
    cssMode: true,
    speed: 600,
    breakpoints: {
      320: {
        slidesPerView: 1,
        slidesPerGroup: 1,
        spaceBetween: 30
      },
      640: {
        slidesPerView: 2.2,
        slidesPerGroup: 1,
        spaceBetween: 30
      }
    },
    // slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
};

// const enableSwiperProfiTablet = function () {
//   swiperProfi = new Swiper(".swiper-profi", {
//     mousewheel: false,
//     slidesPerView: 2.2,
//     spaceBetween: 20,
//     parallax: true,
//     loop: true,
//     speed: 1000
//   });
// };

const enableSwiperProfiMobil = function () {
  swiperProfi = new Swiper(".swiper-profi", {
    mousewheel: false,
    parallax: true,
    loop: true,
    speed: 1000,
    breakpoints: {
      320: {
        slidesPerView: 1,
        slidesPerGroup: 1,
        spaceBetween: 30
      },
      640: {
        slidesPerView: 2.2,
        slidesPerGroup: 1,
        spaceBetween: 30
      }
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
};

const breakpointChecker = function () {
//   if (breakpoint.matches === true) {

//     if (swiperPrice !== undefined) swiperPrice.destroy(true, true);

//     return;

// } else if (breakpoint.matches === false) {

//     enableSwiper();
// }

if (breakpointTablet.matches === false) {
    if (swiperGallery !== undefined) swiperGallery.destroy(true, true);
    if (swiperProfi !== undefined) swiperProfi.destroy(true, true);
    enableSwiperGallery();
    return;

} else if (breakpointTablet.matches === true) {

  enableSwiperGalleryMobile();
  enableSwiperProfiMobil();
}

  
};

breakpoint.addListener(breakpointChecker);
breakpointTablet.addListener(breakpointChecker);

breakpointChecker();

const swiper = new Swiper(".swiper-hero", {
  mousewheel: false,
  parallax: true,
  loop: true,
  speed: 2000,
  pagination: {
    el: ".swiper-hero-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 6000,
  },
});

// const swiperProfi = new Swiper(".swiper-profi", {
//   mousewheel: false,
//   parallax: true,
//   loop: true,
//   speed: 1000,
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// });
