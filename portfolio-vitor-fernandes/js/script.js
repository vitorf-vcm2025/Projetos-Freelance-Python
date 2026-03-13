// Inicia a biblioteca de Animação ao Rolar (AOS)
AOS.init({
  duration: 800,
});

// Inicia e configura o particles.js
particlesJS("particles-js", {
  particles: {
    number: {
      value: 80, // Quantidade de partículas
      density: {
        enable: true,
        value_area: 800,
      },
    },
    color: {
      value: "#00f7ff", // Cor primária das partículas (ciano)
    },
    shape: {
      type: "circle",
    },
    opacity: {
      value: 0.5,
      random: false,
    },
    size: {
      value: 3,
      random: true,
    },
    line_linked: {
      enable: true,
      distance: 150,
      color: "#f500ff", // Cor secundária das linhas (magenta)
      opacity: 0.4,
      width: 1,
    },
    move: {
      enable: true,
      speed: 4, // Velocidade do movimento
      direction: "none",
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
    },
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: {
        enable: true,
        mode: "repulse", // Efeito ao passar o mouse
      },
      onclick: {
        enable: true,
        mode: "push", // Efeito ao clicar
      },
      resize: true,
    },
  },
  retina_detect: true,
});
