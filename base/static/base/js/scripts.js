

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
//login register transition
document.addEventListener('DOMContentLoaded', () => {
  const toReg = document.getElementById('to-register');
  const toLog = document.getElementById('to-login');
  const formBox = document.querySelector('.form-box');
  const wave = document.querySelector('.wave-panel');
  const login = document.getElementById('login-form');
  const register = document.getElementById('register-form');
  const waveText = document.getElementById('wave-content');

  toReg.onclick = e => {
    e.preventDefault();
    formBox.style.left = '-50%';
    wave.style.right = '50%';
    login.classList.remove('active'); register.classList.add('active');
    waveText.innerHTML = '<h3>Hello, Friend!</h3><p>Register and join us today.</p>';
  };

  toLog.onclick = e => {
    e.preventDefault();
    formBox.style.left = '0';
    wave.style.right = '0';
    register.classList.remove('active'); login.classList.add('active');
    waveText.innerHTML = '<h3>Welcome Back!</h3><p>Login to access your account.</p>';
  };
});
