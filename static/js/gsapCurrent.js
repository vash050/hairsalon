// index page

console.log('idea');

const heroBlocks = document.getElementsByClassName("gsap-hero");

window.addEventListener("load", revealAnim);

function revealAnim() {
  const TLFADE = gsap.timeline();

  TLFADE.from(
    heroBlocks,
    { autoAlpha: 0, y: 150, duration: 1.4, stagger: 0.5 },
    "-=0.2"
  );
}

// about us page

const allBlocs = document.querySelectorAll(".bloc");

gsap.utils.toArray([".bloc1", ".bloc2", ".bloc3"]).forEach((bloc, index) => {
  gsap.to(bloc, {
    // autoAlpha:0,
    x: 0,
    // ease: "linear",
    ease: "ease-out",
    duration: 1.4,
    scrollTrigger: {
      trigger: ".bloc-start",
    //   start: "top bottom-=50%",
      start: "top",
      end: "top center-=150",
      // end: `+=${offsets[index]}`,
    //   markers: true,
      // scrub: 5,
    },
  });
});

allBlocs.forEach((bloc, index) => {
  if (index === 3) {
    ScrollTrigger.create({
      trigger: bloc,
      start: "top+=350 center",
    //   start: "top center",
      onEnter: () => {
        bloc.classList.add("active");
      },
      onLeaveBack: () => {
        bloc.classList.remove("active");
      },
      // markers: true,
    });

    return;
  }

  ScrollTrigger.create({
    trigger: bloc,
    start: "top center+=50%",
    onEnter: () => {
      bloc.classList.add("active");
    },
    onLeaveBack: () => {
      bloc.classList.remove("active");
    },
    // markers: true,
  });
});
