

  // JS to trigger counters
  document.addEventListener('DOMContentLoaded', () => {
    const counters = document.querySelectorAll('.counter');
    const speed = 400;

    const animateCounter = counter => {
      const target = +counter.dataset.target;
      const update = () => {
        const current = +counter.innerText;
        const inc = target / speed;
        if (current < target) {
          counter.innerText = Math.ceil(current + inc);
          requestAnimationFrame(update); // smoother than setTimeout
        } else {
          counter.innerText = target;
        }
      };
      update();
    };

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          obs.unobserve(entry.target); // animate only once
        }
      });
    }, { threshold: 1.0 }); // fully visible before animating

    counters.forEach(counter => observer.observe(counter));
  });


  //for reviews animation
  // counters.js
document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter');
  const speed = 400;

  const animateCounter = counter => {
    const target = +counter.dataset.target;
    const update = () => {
      const current = +counter.innerText;
      const inc = target / speed;
      if (current < target) {
        counter.innerText = Math.ceil(current + inc);
        requestAnimationFrame(update);
      } else {
        counter.innerText = target;
      }
    };
    update();
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 1.0 });

  counters.forEach(counter => observer.observe(counter));
});
