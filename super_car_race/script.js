const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const scoreEl = document.getElementById("score");
const levelEl = document.getElementById("level");
const speedEl = document.getElementById("speed");
const healthTextEl = document.getElementById("healthText");
const healthBarEl = document.getElementById("healthBar");
const finalScoreEl = document.getElementById("finalScore");

const startScreen = document.getElementById("startScreen");
const pauseScreen = document.getElementById("pauseScreen");
const gameOverScreen = document.getElementById("gameOverScreen");

const startBtn = document.getElementById("startBtn");
const restartBtn = document.getElementById("restartBtn");

const leftBtn = document.getElementById("leftBtn");
const rightBtn = document.getElementById("rightBtn");
const nitroBtn = document.getElementById("nitroBtn");

const W = canvas.width;
const H = canvas.height;

const road = {
  x: 90,
  width: 300,
  laneCount: 3
};
road.laneWidth = road.width / road.laneCount;

let gameRunning = false;
let paused = false;
let animationId = null;
let frame = 0;
let score = 0;
let level = 1;
let baseSpeed = 7;
let speed = 7;
let health = 100;
let shake = 0;
let roadOffset = 0;
let nitroEnergy = 100;
let nitroActive = false;
let flash = 0;

const keys = {
  left: false,
  right: false,
  nitro: false
};

const player = {
  x: road.x + road.laneWidth + 25,
  y: 620,
  width: 50,
  height: 105,
  color: "#00eaff",
  moveSpeed: 8
};

let enemies = [];
let particles = [];
let stars = [];
let coins = [];
let mountains = [];

function resetGame() {
  frame = 0;
  score = 0;
  level = 1;
  baseSpeed = 7;
  speed = 7;
  health = 100;
  shake = 0;
  roadOffset = 0;
  nitroEnergy = 100;
  nitroActive = false;
  flash = 0;

  enemies = [];
  particles = [];
  coins = [];
  stars = [];
  mountains = [];

  player.x = road.x + road.laneWidth + 25;

  createStars();
  createMountains();
  updateHUD();
}

function createStars() {
  for (let i = 0; i < 70; i++) {
    stars.push({
      x: Math.random() * W,
      y: Math.random() * 240,
      r: Math.random() * 2 + 0.5,
      a: Math.random()
    });
  }
}

function createMountains() {
  let x = 0;
  while (x < W + 100) {
    const w = 100 + Math.random() * 120;
    const h = 40 + Math.random() * 90;
    mountains.push({ x, w, h });
    x += w * 0.7;
  }
}

function updateHUD() {
  scoreEl.textContent = Math.floor(score);
  levelEl.textContent = level;
  speedEl.textContent = speed.toFixed(1);
  healthTextEl.textContent = Math.max(0, Math.floor(health));
  healthBarEl.style.width = Math.max(0, health) + "%";
}

function drawBackground() {
  const sky = ctx.createLinearGradient(0, 0, 0, H);
  sky.addColorStop(0, "#081229");
  sky.addColorStop(0.35, "#132850");
  sky.addColorStop(0.65, "#10151f");
  sky.addColorStop(1, "#050608");
  ctx.fillStyle = sky;
  ctx.fillRect(0, 0, W, H);

  for (const s of stars) {
    s.a += 0.03;
    ctx.fillStyle = `rgba(255,255,255,${0.4 + Math.sin(s.a) * 0.4})`;
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
    ctx.fill();
  }

  ctx.fillStyle = "#f4c542";
  ctx.beginPath();
  ctx.arc(W - 80, 90, 35, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#1d2540";
  mountains.forEach(m => {
    ctx.beginPath();
    ctx.moveTo(m.x, 260);
    ctx.lineTo(m.x + m.w / 2, 260 - m.h);
    ctx.lineTo(m.x + m.w, 260);
    ctx.closePath();
    ctx.fill();
  });

  ctx.fillStyle = "#0b3d1f";
  ctx.fillRect(0, 260, road.x, H - 260);
  ctx.fillRect(road.x + road.width, 260, W - road.x - road.width, H - 260);

  for (let y = 280; y < H; y += 45) {
    ctx.fillStyle = y % 90 === 0 ? "#1f6d2a" : "#2f913b";
    ctx.fillRect(0, y + (frame * 2 % 45), road.x, 20);
    ctx.fillRect(road.x + road.width, y + (frame * 2 % 45), W - road.x - road.width, 20);
  }
}

function drawRoad() {
  ctx.fillStyle = "#252525";
  ctx.fillRect(road.x, 0, road.width, H);

  ctx.fillStyle = "#ffffff";
  ctx.fillRect(road.x, 0, 6, H);
  ctx.fillRect(road.x + road.width - 6, 0, 6, H);

  for (let i = 1; i < road.laneCount; i++) {
    for (let y = -60 + roadOffset; y < H; y += 100) {
      ctx.fillStyle = "#e9e9e9";
      ctx.fillRect(road.x + i * road.laneWidth - 4, y, 8, 50);
    }
  }

  for (let y = 0; y < H; y += 35) {
    ctx.fillStyle = ((y + Math.floor(roadOffset)) / 35) % 2 < 1 ? "#ff3355" : "#44f7ff";
    ctx.fillRect(road.x - 10, y, 10, 18);
    ctx.fillRect(road.x + road.width, y, 10, 18);
  }

  ctx.strokeStyle = "rgba(0,255,255,0.15)";
  ctx.lineWidth = 18;
  ctx.strokeRect(road.x + 9, 0, road.width - 18, H);
}

function roundRect(x, y, w, h, r, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + r);
  ctx.lineTo(x + w, y + h - r);
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  ctx.lineTo(x + r, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - r);
  ctx.lineTo(x, y + r);
  ctx.quadraticCurveTo(x, y, x + r, y);
  ctx.closePath();
  ctx.fill();
}

function drawCar(x, y, w, h, color, isPlayer = false) {
  ctx.save();

  if (isPlayer) {
    ctx.shadowColor = color;
    ctx.shadowBlur = 25;
  }

  roundRect(x, y, w, h, 12, color);

  ctx.fillStyle = "#0b0f18";
  roundRect(x + 9, y + 10, w - 18, 20, 7, "#0b0f18");
  roundRect(x + 11, y + 55, w - 22, 18, 7, "#0b0f18");

  ctx.fillStyle = "#fffbcc";
  ctx.fillRect(x + 7, y + 6, 9, 8);
  ctx.fillRect(x + w - 16, y + 6, 9, 8);

  ctx.fillStyle = "#ff3344";
  ctx.fillRect(x + 7, y + h - 14, 9, 8);
  ctx.fillRect(x + w - 16, y + h - 14, 9, 8);

  ctx.fillStyle = "#111";
  ctx.fillRect(x - 4, y + 18, 6, 20);
  ctx.fillRect(x - 4, y + h - 38, 6, 20);
  ctx.fillRect(x + w - 2, y + 18, 6, 20);
  ctx.fillRect(x + w - 2, y + h - 38, 6, 20);

  if (isPlayer) {
    const flameHeight = nitroActive ? 30 : 16;
    ctx.fillStyle = nitroActive ? "#ff9b00" : "#ff5a00";
    ctx.beginPath();
    ctx.moveTo(x + w / 2 - 10, y + h);
    ctx.lineTo(x + w / 2, y + h + flameHeight + Math.sin(frame * 0.5) * 6);
    ctx.lineTo(x + w / 2 + 10, y + h);
    ctx.closePath();
    ctx.fill();
  }

  ctx.restore();
}

function spawnEnemy() {
  const lane = Math.floor(Math.random() * road.laneCount);
  const colors = ["#ff3b3b", "#ffd93b", "#4dff88", "#c44dff", "#ff8c42"];
  enemies.push({
    x: road.x + lane * road.laneWidth + (road.laneWidth - 50) / 2,
    y: -130,
    width: 50,
    height: 105,
    speed: baseSpeed + Math.random() * 3 + level * 0.3,
    color: colors[Math.floor(Math.random() * colors.length)]
  });
}

function spawnCoin() {
  const lane = Math.floor(Math.random() * road.laneCount);
  coins.push({
    x: road.x + lane * road.laneWidth + road.laneWidth / 2,
    y: -30,
    r: 12,
    speed: baseSpeed + 2,
    spin: Math.random() * Math.PI * 2
  });
}

function drawCoin(c) {
  c.spin += 0.2;
  const scaleX = Math.abs(Math.cos(c.spin));
  ctx.save();
  ctx.translate(c.x, c.y);
  ctx.scale(scaleX, 1);
  ctx.shadowColor = "#ffd700";
  ctx.shadowBlur = 18;
  ctx.fillStyle = "#ffd700";
  ctx.beginPath();
  ctx.arc(0, 0, c.r, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#fff2a8";
  ctx.beginPath();
  ctx.arc(0, 0, c.r / 2, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}

function createParticles(x, y, color, count = 18) {
  for (let i = 0; i < count; i++) {
    particles.push({
      x,
      y,
      dx: (Math.random() - 0.5) * 8,
      dy: (Math.random() - 0.5) * 8,
      size: Math.random() * 5 + 2,
      life: 35,
      color
    });
  }
}

function updateParticles() {
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.dx;
    p.y += p.dy;
    p.dy += 0.05;
    p.life--;
    p.size *= 0.97;
    if (p.life <= 0 || p.size < 0.4) particles.splice(i, 1);
  }
}

function drawParticles() {
  for (const p of particles) {
    ctx.fillStyle = `${p.color}${Math.floor((p.life / 35) * 255).toString(16).padStart(2, "0")}`;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

function updatePlayer() {
  if (keys.left) player.x -= player.moveSpeed;
  if (keys.right) player.x += player.moveSpeed;

  if (keys.nitro && nitroEnergy > 0) {
    nitroActive = true;
    nitroEnergy -= 0.7;
  } else {
    nitroActive = false;
    nitroEnergy += 0.25;
  }

  nitroEnergy = Math.max(0, Math.min(100, nitroEnergy));

  speed = nitroActive ? baseSpeed + 5 : baseSpeed;

  const minX = road.x + 8;
  const maxX = road.x + road.width - player.width - 8;

  if (player.x < minX) player.x = minX;
  if (player.x > maxX) player.x = maxX;

  if (nitroActive && frame % 3 === 0) {
    createParticles(player.x + player.width / 2, player.y + player.height, "#ff9900", 2);
  }
}

function updateEnemies() {
  for (let i = enemies.length - 1; i >= 0; i--) {
    enemies[i].y += enemies[i].speed + (nitroActive ? 2 : 0);

    if (enemies[i].y > H + 150) {
      enemies.splice(i, 1);
      score += 10;
    }
  }
}

function updateCoins() {
  for (let i = coins.length - 1; i >= 0; i--) {
    coins[i].y += coins[i].speed;

    if (coins[i].y > H + 50) {
      coins.splice(i, 1);
    }
  }
}

function rectHit(a, b) {
  return (
    a.x < b.x + b.width &&
    a.x + a.width > b.x &&
    a.y < b.y + b.height &&
    a.y + a.height > b.y
  );
}

function circleRectHit(circle, rect) {
  const dx = Math.abs(circle.x - (rect.x + rect.width / 2));
  const dy = Math.abs(circle.y - (rect.y + rect.height / 2));

  if (dx > rect.width / 2 + circle.r) return false;
  if (dy > rect.height / 2 + circle.r) return false;

  if (dx <= rect.width / 2) return true;
  if (dy <= rect.height / 2) return true;

  const cx = dx - rect.width / 2;
  const cy = dy - rect.height / 2;

  return cx * cx + cy * cy <= circle.r * circle.r;
}

function handleCollisions() {
  for (let i = enemies.length - 1; i >= 0; i--) {
    if (rectHit(player, enemies[i])) {
      createParticles(player.x + player.width / 2, player.y + player.height / 2, "#ff4444", 30);
      enemies.splice(i, 1);
      health -= 20;
      shake = 10;
      flash = 6;
      if (health <= 0) {
        endGame();
        return;
      }
    }
  }

  for (let i = coins.length - 1; i >= 0; i--) {
    if (circleRectHit(coins[i], player)) {
      createParticles(coins[i].x, coins[i].y, "#ffd700", 16);
      coins.splice(i, 1);
      score += 50;
      health = Math.min(100, health + 5);
    }
  }
}

function drawNitroBar() {
  const x = 15;
  const y = H - 25;
  const w = 130;
  const h = 12;

  ctx.fillStyle = "rgba(255,255,255,0.18)";
  roundRect(x, y, w, h, 8, "rgba(255,255,255,0.18)");

  const fillW = (nitroEnergy / 100) * w;
  roundRect(x, y, fillW, h, 8, nitroActive ? "#ff8c00" : "#00eaff");

  ctx.fillStyle = "#fff";
  ctx.font = "bold 13px Arial";
  ctx.fillText("NITRO", x, y - 6);
}

function drawEffects() {
  if (flash > 0) {
    ctx.fillStyle = `rgba(255,255,255,${flash * 0.08})`;
    ctx.fillRect(0, 0, W, H);
    flash--;
  }
}

function drawLevelText() {
  ctx.fillStyle = "rgba(255,255,255,0.14)";
  ctx.font = "bold 50px Arial";
  ctx.fillText("LEVEL " + level, W / 2 - 100, 100);
}

function updateDifficulty() {
  level = 1 + Math.floor(score / 300);
  baseSpeed = 7 + level * 0.35;
}

function drawScene() {
  let dx = 0;
  let dy = 0;

  if (shake > 0) {
    dx = (Math.random() - 0.5) * shake;
    dy = (Math.random() - 0.5) * shake;
    shake *= 0.85;
  }

  ctx.save();
  ctx.translate(dx, dy);

  drawBackground();
  drawRoad();
  drawLevelText();

  for (const c of coins) drawCoin(c);
  for (const e of enemies) drawCar(e.x, e.y, e.width, e.height, e.color, false);

  drawCar(player.x, player.y, player.width, player.height, player.color, true);
  drawParticles();
  drawNitroBar();
  drawEffects();

  ctx.restore();
}

function loop() {
  if (!gameRunning || paused) return;

  frame++;
  roadOffset += speed;
  if (roadOffset >= 100) roadOffset = 0;

  ctx.clearRect(0, 0, W, H);

  updateDifficulty();
  updatePlayer();
  updateEnemies();
  updateCoins();
  updateParticles();
  handleCollisions();

  if (frame % Math.max(22, 58 - level * 2) === 0) spawnEnemy();
  if (frame % 120 === 0) spawnCoin();

  score += nitroActive ? 0.35 : 0.2;

  drawScene();
  updateHUD();

  animationId = requestAnimationFrame(loop);
}

function startGame() {
  resetGame();
  startScreen.classList.remove("show");
  pauseScreen.classList.remove("show");
  gameOverScreen.classList.remove("show");
  gameRunning = true;
  paused = false;
  loop();
}

function endGame() {
  gameRunning = false;
  finalScoreEl.textContent = Math.floor(score);
  gameOverScreen.classList.add("show");
  cancelAnimationFrame(animationId);
}

function togglePause() {
  if (!gameRunning) return;
  paused = !paused;
  if (paused) {
    pauseScreen.classList.add("show");
    cancelAnimationFrame(animationId);
  } else {
    pauseScreen.classList.remove("show");
    loop();
  }
}

document.addEventListener("keydown", e => {
  const k = e.key.toLowerCase();
  if (k === "arrowleft" || k === "a") keys.left = true;
  if (k === "arrowright" || k === "d") keys.right = true;
  if (k === " ") {
    e.preventDefault();
    keys.nitro = true;
  }
  if (k === "p") togglePause();
});

document.addEventListener("keyup", e => {
  const k = e.key.toLowerCase();
  if (k === "arrowleft" || k === "a") keys.left = false;
  if (k === "arrowright" || k === "d") keys.right = false;
  if (k === " ") keys.nitro = false;
});

function pressLeft(on) { keys.left = on; }
function pressRight(on) { keys.right = on; }
function pressNitro(on) { keys.nitro = on; }

leftBtn.addEventListener("mousedown", () => pressLeft(true));
leftBtn.addEventListener("mouseup", () => pressLeft(false));
leftBtn.addEventListener("mouseleave", () => pressLeft(false));

rightBtn.addEventListener("mousedown", () => pressRight(true));
rightBtn.addEventListener("mouseup", () => pressRight(false));
rightBtn.addEventListener("mouseleave", () => pressRight(false));

nitroBtn.addEventListener("mousedown", () => pressNitro(true));
nitroBtn.addEventListener("mouseup", () => pressNitro(false));
nitroBtn.addEventListener("mouseleave", () => pressNitro(false));

leftBtn.addEventListener("touchstart", e => { e.preventDefault(); pressLeft(true); });
leftBtn.addEventListener("touchend", e => { e.preventDefault(); pressLeft(false); });

rightBtn.addEventListener("touchstart", e => { e.preventDefault(); pressRight(true); });
rightBtn.addEventListener("touchend", e => { e.preventDefault(); pressRight(false); });

nitroBtn.addEventListener("touchstart", e => { e.preventDefault(); pressNitro(true); });
nitroBtn.addEventListener("touchend", e => { e.preventDefault(); pressNitro(false); });

startBtn.addEventListener("click", startGame);
restartBtn.addEventListener("click", startGame);

resetGame();