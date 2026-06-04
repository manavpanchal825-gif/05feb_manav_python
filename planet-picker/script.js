const planets = [
  { name: "Mercury", img: "https://space-facts.com/wp-content/uploads/mercury.png", desc: "Closest planet", color: "#aaa" },
  { name: "Venus", img: "https://space-facts.com/wp-content/uploads/venus.png", desc: "Hottest planet", color: "#f5c16c" },
  { name: "Earth", img: "https://space-facts.com/wp-content/uploads/earth.png", desc: "Our home planet", color: "#00d9ff" },
  { name: "Mars", img: "https://space-facts.com/wp-content/uploads/mars.png", desc: "Red planet", color: "#ff4d4d" },
  { name: "Jupiter", img: "https://space-facts.com/wp-content/uploads/jupiter.png", desc: "Largest planet", color: "#f39c12" },
  { name: "Saturn", img: "https://space-facts.com/wp-content/uploads/saturn.png", desc: "Ring planet", color: "#f1c40f" },
  { name: "Uranus", img: "https://space-facts.com/wp-content/uploads/uranus.png", desc: "Ice giant", color: "#00ffff" },
  { name: "Neptune", img: "https://space-facts.com/wp-content/uploads/neptune.png", desc: "Farthest planet", color: "#0044ff" }
];

let index = 2;

const img = document.getElementById("planetImg");
const planetName = document.getElementById("planetName");
const desc = document.getElementById("planetDesc");
const buttons = document.querySelectorAll(".planet-buttons span");

function updatePlanet(i) {
  const p = planets[i];

  img.src = p.img;
  planetName.innerText = p.name;
  desc.innerText = p.desc;

  img.style.boxShadow = `0 0 60px ${p.color}, 0 0 120px ${p.color}`;

  buttons.forEach(btn => btn.classList.remove("active"));
  buttons[i].classList.add("active");
}

// Click buttons
buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    index = parseInt(btn.dataset.index);
    updatePlanet(index);
  });
});

// Scroll change
window.addEventListener("wheel", (e) => {
  if (e.deltaY > 0) index++;
  else index--;

  if (index < 0) index = planets.length - 1;
  if (index >= planets.length) index = 0;

  updatePlanet(index);
});

// First load
updatePlanet(index);