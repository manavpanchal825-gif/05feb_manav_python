import pygame
import random
import math
import json
import os
import sys

pygame.init()
try:
    pygame.mixer.init()
    SOUND_AVAILABLE = True
except pygame.error:
    SOUND_AVAILABLE = False

# =========================================================
# WINDOW
# =========================================================
WIDTH, HEIGHT = 1200, 760
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Strike Pro")
clock = pygame.time.Clock()
FPS = 60

# =========================================================
# PATHS
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMG_DIR = os.path.join(ASSETS_DIR, "images")
SND_DIR = os.path.join(ASSETS_DIR, "sounds")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
SAVE_FILE = os.path.join(DATA_DIR, "save.json")

os.makedirs(DATA_DIR, exist_ok=True)

# =========================================================
# COLORS
# =========================================================
WHITE = (255, 255, 255)
BLACK = (10, 10, 20)
NAVY = (15, 20, 40)
CYAN = (0, 255, 255)
YELLOW = (255, 230, 70)
RED = (255, 70, 70)
GREEN = (80, 240, 120)
ORANGE = (255, 160, 60)
PURPLE = (180, 100, 255)
GRAY = (120, 120, 120)
DARK = (35, 35, 50)
BLUE = (90, 170, 255)

# =========================================================
# FONTS
# =========================================================
title_font = pygame.font.SysFont("arial", 54, bold=True)
big_font = pygame.font.SysFont("arial", 32, bold=True)
ui_font = pygame.font.SysFont("arial", 24, bold=True)
small_font = pygame.font.SysFont("arial", 18, bold=True)

# =========================================================
# STATES
# =========================================================
MENU = "menu"
PLAYING = "playing"
PAUSED = "paused"
SHOP = "shop"
GAME_OVER = "game_over"
VICTORY = "victory"

# =========================================================
# SAVE / LOAD
# =========================================================
DEFAULT_SAVE = {
    "coins": 0,
    "damage_level": 1,
    "fire_rate_level": 1,
    "max_health_level": 1,
    "shield_level": 1
}

def load_save():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key in DEFAULT_SAVE:
                    if key not in data:
                        data[key] = DEFAULT_SAVE[key]
                return data
        except Exception:
            return DEFAULT_SAVE.copy()
    return DEFAULT_SAVE.copy()

def save_game_data(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

SAVE_DATA = load_save()

# =========================================================
# ASSET HELPERS
# =========================================================
def load_image(filename, size=None):
    path = os.path.join(IMG_DIR, filename)
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img
    return None

def load_sound(filename):
    if not SOUND_AVAILABLE:
        return None
    path = os.path.join(SND_DIR, filename)
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    return None

def play_sound(sound):
    if sound is not None:
        sound.play()

shoot_sound = load_sound("shoot.wav")
explosion_sound = load_sound("explosion.wav")
hit_sound = load_sound("hit.wav")
powerup_sound = load_sound("powerup.wav")

music_path = os.path.join(SND_DIR, "music.mp3")
if SOUND_AVAILABLE and os.path.exists(music_path):
    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

# =========================================================
# IMAGE ASSETS
# =========================================================
player_img = load_image("player.png", (70, 70))
enemy1_img = load_image("enemy1.png", (55, 55))
enemy2_img = load_image("enemy2.png", (65, 65))
boss1_img = load_image("boss1.png", (220, 130))
boss2_img = load_image("boss2.png", (260, 150))
bg_img = load_image("bg.png", (WIDTH, HEIGHT))
button_img = load_image("button.png", (240, 70))

# =========================================================
# HELPERS
# =========================================================
def draw_text(text, font, color, x, y, center=False):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(img, rect)

def clamp(value, low, high):
    return max(low, min(value, high))

# =========================================================
# BUTTON
# =========================================================
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.hover_scale = 1.0

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        hovered = self.rect.collidepoint(mouse_pos)

        target_scale = 1.05 if hovered else 1.0
        self.hover_scale += (target_scale - self.hover_scale) * 0.2

        draw_rect = self.rect.copy()
        draw_rect.width = int(self.rect.width * self.hover_scale)
        draw_rect.height = int(self.rect.height * self.hover_scale)
        draw_rect.center = self.rect.center

        if button_img:
            img = pygame.transform.scale(button_img, (draw_rect.width, draw_rect.height))
            screen.blit(img, draw_rect)
        else:
            pygame.draw.rect(screen, CYAN if hovered else BLUE, draw_rect, border_radius=14)
            pygame.draw.rect(screen, WHITE, draw_rect, 2, border_radius=14)

        draw_text(self.text, ui_font, WHITE, draw_rect.centerx, draw_rect.centery, center=True)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)

# =========================================================
# STAR
# =========================================================
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(1, 4)
        self.size = random.randint(1, 3)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# =========================================================
# PARTICLE
# =========================================================
class Particle:
    def __init__(self, x, y, color):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)
        self.x = x
        self.y = y
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.life = random.randint(15, 30)
        self.color = color
        self.radius = random.randint(2, 5)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

    def draw(self):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# =========================================================
# PLAYER
# =========================================================
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 6
        self.width = 60
        self.height = 60

        self.damage = SAVE_DATA["damage_level"]
        self.fire_rate = max(4, 14 - SAVE_DATA["fire_rate_level"] * 2)
        self.max_health = 100 + (SAVE_DATA["max_health_level"] - 1) * 20
        self.health = self.max_health
        self.shield_duration = 180 + (SAVE_DATA["shield_level"] - 1) * 40

        self.cooldown = 0
        self.flash_timer = 0
        self.shield_timer = 0
        self.score = 0
        self.coins = 0
        self.lives = 3

    @property
    def rect(self):
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        self.x = clamp(self.x, 40, WIDTH - 40)
        self.y = clamp(self.y, HEIGHT // 2, HEIGHT - 40)

        if self.cooldown > 0:
            self.cooldown -= 1
        if self.flash_timer > 0:
            self.flash_timer -= 1
        if self.shield_timer > 0:
            self.shield_timer -= 1

    def shoot(self, bullets):
        if self.cooldown == 0:
            bullets.append(Bullet(self.x, self.y - 30, -11, "player", self.damage))
            self.cooldown = self.fire_rate
            play_sound(shoot_sound)

    def take_damage(self, amount):
        if self.shield_timer > 0:
            return False

        self.health -= amount
        self.flash_timer = 10
        play_sound(hit_sound)

        if self.health <= 0:
            self.lives -= 1
            if self.lives > 0:
                self.health = self.max_health
                self.x = WIDTH // 2
                self.y = HEIGHT - 100
                self.shield_timer = self.shield_duration
            else:
                return True
        return False

    def draw(self):
        if player_img:
            screen.blit(player_img, player_img.get_rect(center=(self.x, self.y)))
        else:
            color = WHITE if self.flash_timer % 2 else CYAN
            pygame.draw.polygon(screen, color, [
                (self.x, self.y - 30),
                (self.x - 22, self.y + 20),
                (self.x + 22, self.y + 20),
            ])
            pygame.draw.polygon(screen, BLUE, [
                (self.x - 20, self.y + 5),
                (self.x - 35, self.y + 22),
                (self.x - 8, self.y + 22),
            ])
            pygame.draw.polygon(screen, BLUE, [
                (self.x + 20, self.y + 5),
                (self.x + 35, self.y + 22),
                (self.x + 8, self.y + 22),
            ])

        if self.shield_timer > 0:
            pygame.draw.circle(screen, CYAN, (self.x, self.y), 40, 2)

# =========================================================
# BULLET
# =========================================================
class Bullet:
    def __init__(self, x, y, speed, owner, damage):
        self.x = x
        self.y = y
        self.speed = speed
        self.owner = owner
        self.damage = damage
        self.radius = 5 if owner == "player" else 6

    @property
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        self.y += self.speed

    def draw(self):
        color = YELLOW if self.owner == "player" else ORANGE
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), max(1, self.radius // 2))

# =========================================================
# ENEMY
# =========================================================
class Enemy:
    def __init__(self, level):
        self.type = random.choice(["basic", "fast", "tank"])
        self.x = random.randint(60, WIDTH - 60)
        self.y = random.randint(-300, -40)
        self.fire_timer = random.randint(40, 120)

        if self.type == "basic":
            self.health = 2 + level
            self.speed = random.uniform(2, 3.5)
            self.color = RED
            self.damage = 10
            self.img = enemy1_img

        elif self.type == "fast":
            self.health = 1 + level
            self.speed = random.uniform(3.5, 5)
            self.color = PURPLE
            self.damage = 12
            self.img = enemy1_img

        else:
            self.health = 5 + level * 2
            self.speed = random.uniform(1.5, 2.5)
            self.color = ORANGE
            self.damage = 15
            self.img = enemy2_img

        self.dx = random.choice([-2, -1, 1, 2])

    @property
    def rect(self):
        return pygame.Rect(self.x - 25, self.y - 25, 50, 50)

    def update(self, bullets):
        self.x += self.dx
        self.y += self.speed

        if self.x < 30 or self.x > WIDTH - 30:
            self.dx *= -1

        self.fire_timer -= 1
        if self.fire_timer <= 0:
            bullets.append(Bullet(self.x, self.y + 20, 7, "enemy", self.damage))
            self.fire_timer = random.randint(80, 150)

        if self.y > HEIGHT + 40:
            self.y = random.randint(-250, -40)
            self.x = random.randint(60, WIDTH - 60)

    def draw(self):
        if self.img:
            screen.blit(self.img, self.img.get_rect(center=(self.x, self.y)))
        else:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 24)
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 10)

# =========================================================
# BOSSES
# =========================================================
class Boss:
    def __init__(self, boss_type, level):
        self.boss_type = boss_type
        self.x = WIDTH // 2
        self.y = 120
        self.fire_timer = 0
        self.health = 150 + level * 40
        self.max_health = self.health

        if boss_type == 1:
            self.dx = 4
            self.damage = 15
            self.img = boss1_img
            self.width = 220
            self.height = 130
        else:
            self.dx = 5
            self.damage = 20
            self.img = boss2_img
            self.width = 260
            self.height = 150

    @property
    def rect(self):
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def update(self, bullets):
        self.x += self.dx
        if self.x < 150 or self.x > WIDTH - 150:
            self.dx *= -1

        self.fire_timer += 1

        if self.boss_type == 1:
            if self.fire_timer >= 25:
                bullets.append(Bullet(self.x - 50, self.y + 25, 8, "enemy", self.damage))
                bullets.append(Bullet(self.x, self.y + 25, 9, "enemy", self.damage))
                bullets.append(Bullet(self.x + 50, self.y + 25, 8, "enemy", self.damage))
                self.fire_timer = 0
        else:
            if self.fire_timer >= 18:
                for dx in [-3, -1.5, 0, 1.5, 3]:
                    b = SpreadBullet(self.x, self.y + 30, dx, 7, self.damage)
                    bullets.append(b)
                self.fire_timer = 0

    def draw(self):
        if self.img:
            screen.blit(self.img, self.img.get_rect(center=(self.x, self.y)))
        else:
            pygame.draw.rect(screen, RED if self.boss_type == 1 else PURPLE, self.rect, border_radius=20)
            pygame.draw.rect(screen, WHITE, (self.x - 35, self.y - 10, 70, 20), border_radius=8)

# =========================================================
# SPREAD BULLET
# =========================================================
class SpreadBullet(Bullet):
    def __init__(self, x, y, dx, dy, damage):
        super().__init__(x, y, dy, "enemy", damage)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy

# =========================================================
# POWERUP
# =========================================================
class PowerUp:
    def __init__(self):
        self.kind = random.choice(["health", "shield", "coins"])
        self.x = random.randint(40, WIDTH - 40)
        self.y = -20
        self.size = 24
        self.speed = 3

    @property
    def rect(self):
        return pygame.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)

    def update(self):
        self.y += self.speed

    def draw(self):
        color = GREEN if self.kind == "health" else CYAN if self.kind == "shield" else YELLOW
        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=6)

# =========================================================
# GAME
# =========================================================
class Game:
    def __init__(self):
        self.stars = [Star() for _ in range(100)]
        self.menu_buttons = [
            Button(WIDTH // 2 - 120, 280, 240, 65, "Start Game"),
            Button(WIDTH // 2 - 120, 370, 240, 65, "Shop"),
            Button(WIDTH // 2 - 120, 460, 240, 65, "Quit"),
        ]
        self.shop_buttons = [
            Button(150, 180, 360, 55, "Upgrade Damage - 50 Coins"),
            Button(150, 260, 360, 55, "Upgrade Fire Rate - 60 Coins"),
            Button(150, 340, 360, 55, "Upgrade Max Health - 70 Coins"),
            Button(150, 420, 360, 55, "Upgrade Shield - 80 Coins"),
            Button(150, 530, 220, 55, "Back"),
        ]
        self.reset()

    def reset(self):
        self.state = MENU
        self.player = Player()
        self.bullets = []
        self.enemies = []
        self.particles = []
        self.powerups = []
        self.level = 1
        self.kills = 0
        self.kills_needed = 14
        self.boss = None
        self.boss_count = 0
        self.spawn_wave()

    def spawn_wave(self):
        for _ in range(min(5 + self.level * 2, 14)):
            self.enemies.append(Enemy(self.level))

    def make_explosion(self, x, y, color=ORANGE):
        for _ in range(15):
            self.particles.append(Particle(x, y, color))
        play_sound(explosion_sound)

    def buy_upgrade(self, key, cost):
        if SAVE_DATA["coins"] >= cost:
            SAVE_DATA["coins"] -= cost
            SAVE_DATA[key] += 1
            save_game_data(SAVE_DATA)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game_data(SAVE_DATA)
                pygame.quit()
                sys.exit()

            if self.state == MENU:
                if self.menu_buttons[0].is_clicked(event):
                    self.reset()
                    self.state = PLAYING
                elif self.menu_buttons[1].is_clicked(event):
                    self.state = SHOP
                elif self.menu_buttons[2].is_clicked(event):
                    save_game_data(SAVE_DATA)
                    pygame.quit()
                    sys.exit()

            elif self.state == SHOP:
                if self.shop_buttons[0].is_clicked(event):
                    self.buy_upgrade("damage_level", 50)
                elif self.shop_buttons[1].is_clicked(event):
                    self.buy_upgrade("fire_rate_level", 60)
                elif self.shop_buttons[2].is_clicked(event):
                    self.buy_upgrade("max_health_level", 70)
                elif self.shop_buttons[3].is_clicked(event):
                    self.buy_upgrade("shield_level", 80)
                elif self.shop_buttons[4].is_clicked(event):
                    self.state = MENU

            elif self.state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.state = PAUSED
                    elif event.key == pygame.K_SPACE:
                        self.player.shoot(self.bullets)

            elif self.state == PAUSED:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.state = PLAYING

            elif self.state in [GAME_OVER, VICTORY]:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.reset()
                    self.state = MENU

    def update(self):
        for star in self.stars:
            star.update()

        for p in self.particles[:]:
            p.update()
            if p.life <= 0:
                self.particles.remove(p)

        if self.state != PLAYING:
            return

        keys = pygame.key.get_pressed()
        self.player.update(keys)

        if keys[pygame.K_SPACE]:
            self.player.shoot(self.bullets)

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.y < -50 or bullet.y > HEIGHT + 50 or bullet.x < -50 or bullet.x > WIDTH + 50:
                self.bullets.remove(bullet)
                continue

        for enemy in self.enemies[:]:
            enemy.update(self.bullets)

            if enemy.rect.colliderect(self.player.rect):
                self.make_explosion(enemy.x, enemy.y, RED)
                self.enemies.remove(enemy)
                dead = self.player.take_damage(20)
                if dead:
                    SAVE_DATA["coins"] += self.player.coins
                    save_game_data(SAVE_DATA)
                    self.state = GAME_OVER

        if self.boss:
            self.boss.update(self.bullets)

        for bullet in self.bullets[:]:
            if bullet.owner == "player":
                for enemy in self.enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.health -= bullet.damage
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

                        if enemy.health <= 0:
                            self.make_explosion(enemy.x, enemy.y)
                            self.player.score += 10
                            self.player.coins += 5
                            self.kills += 1
                            if random.randint(1, 8) == 1:
                                self.powerups.append(PowerUp())
                            self.enemies.remove(enemy)
                        break

                if self.boss and bullet in self.bullets and bullet.rect.colliderect(self.boss.rect):
                    self.boss.health -= bullet.damage
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

                    if self.boss.health <= 0:
                        self.make_explosion(self.boss.x, self.boss.y, PURPLE)
                        self.player.score += 200
                        self.player.coins += 50
                        self.boss = None
                        self.level += 1
                        self.kills = 0
                        self.boss_count += 1

                        if self.boss_count >= 2:
                            SAVE_DATA["coins"] += self.player.coins
                            save_game_data(SAVE_DATA)
                            self.state = VICTORY
                        else:
                            self.spawn_wave()

            else:
                if bullet.rect.colliderect(self.player.rect):
                    dead = self.player.take_damage(bullet.damage)
                    self.make_explosion(self.player.x, self.player.y, ORANGE)
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if dead:
                        SAVE_DATA["coins"] += self.player.coins
                        save_game_data(SAVE_DATA)
                        self.state = GAME_OVER

        for power in self.powerups[:]:
            power.update()
            if power.y > HEIGHT + 20:
                self.powerups.remove(power)
            elif power.rect.colliderect(self.player.rect):
                if power.kind == "health":
                    self.player.health = min(self.player.max_health, self.player.health + 30)
                elif power.kind == "shield":
                    self.player.shield_timer = self.player.shield_duration
                else:
                    self.player.coins += 20
                play_sound(powerup_sound)
                self.powerups.remove(power)

        if not self.boss and self.kills >= self.kills_needed and len(self.enemies) == 0:
            self.boss = Boss(1 if self.boss_count == 0 else 2, self.level)

    def draw_background(self):
        if bg_img:
            screen.blit(bg_img, (0, 0))
        else:
            screen.fill(NAVY)
            for star in self.stars:
                star.draw()

    def draw_ui(self):
        draw_text(f"Score: {self.player.score}", ui_font, WHITE, 20, 15)
        draw_text(f"Coins: {self.player.coins}", ui_font, YELLOW, 190, 15)
        draw_text(f"Level: {self.level}", ui_font, WHITE, 340, 15)
        draw_text(f"Lives: {self.player.lives}", ui_font, WHITE, 470, 15)

        pygame.draw.rect(screen, DARK, (20, 50, 250, 20), border_radius=8)
        fill = int(250 * (self.player.health / self.player.max_health))
        pygame.draw.rect(screen, GREEN, (20, 50, fill, 20), border_radius=8)
        pygame.draw.rect(screen, WHITE, (20, 50, 250, 20), 2, border_radius=8)

        if self.boss:
            pygame.draw.rect(screen, DARK, (WIDTH // 2 - 180, 15, 360, 18), border_radius=8)
            fill = int(360 * (self.boss.health / self.boss.max_health))
            pygame.draw.rect(screen, RED, (WIDTH // 2 - 180, 15, fill, 18), border_radius=8)
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 180, 15, 360, 18), 2, border_radius=8)
            draw_text("BOSS", small_font, WHITE, WIDTH // 2 - 20, 38)

    def draw(self):
        self.draw_background()

        if self.state == MENU:
            draw_text("GALAXY STRIKE PRO", title_font, CYAN, WIDTH // 2, 160, center=True)
            draw_text(f"Saved Coins: {SAVE_DATA['coins']}", big_font, YELLOW, WIDTH // 2, 220, center=True)
            for b in self.menu_buttons:
                b.draw()

        elif self.state == SHOP:
            draw_text("SHOP / UPGRADES", title_font, GREEN, WIDTH // 2, 90, center=True)
            draw_text(f"Coins: {SAVE_DATA['coins']}", big_font, YELLOW, WIDTH // 2, 135, center=True)
            draw_text(f"Damage Level: {SAVE_DATA['damage_level']}", ui_font, WHITE, 600, 200)
            draw_text(f"Fire Rate Level: {SAVE_DATA['fire_rate_level']}", ui_font, WHITE, 600, 280)
            draw_text(f"Max Health Level: {SAVE_DATA['max_health_level']}", ui_font, WHITE, 600, 360)
            draw_text(f"Shield Level: {SAVE_DATA['shield_level']}", ui_font, WHITE, 600, 440)
            for b in self.shop_buttons:
                b.draw()

        else:
            for power in self.powerups:
                power.draw()
            for enemy in self.enemies:
                enemy.draw()
            if self.boss:
                self.boss.draw()
            for bullet in self.bullets:
                bullet.draw()
            self.player.draw()
            for p in self.particles:
                p.draw()
            self.draw_ui()

            if self.state == PAUSED:
                draw_text("PAUSED", title_font, YELLOW, WIDTH // 2, HEIGHT // 2 - 20, center=True)
                draw_text("Press P to Resume", big_font, WHITE, WIDTH // 2, HEIGHT // 2 + 35, center=True)

            elif self.state == GAME_OVER:
                draw_text("GAME OVER", title_font, RED, WIDTH // 2, HEIGHT // 2 - 40, center=True)
                draw_text(f"Final Score: {self.player.score}", big_font, WHITE, WIDTH // 2, HEIGHT // 2 + 10, center=True)
                draw_text(f"Coins Earned: {self.player.coins}", big_font, YELLOW, WIDTH // 2, HEIGHT // 2 + 55, center=True)
                draw_text("Press R", big_font, WHITE, WIDTH // 2, HEIGHT // 2 + 100, center=True)

            elif self.state == VICTORY:
                draw_text("YOU WIN!", title_font, GREEN, WIDTH // 2, HEIGHT // 2 - 40, center=True)
                draw_text(f"Final Score: {self.player.score}", big_font, WHITE, WIDTH // 2, HEIGHT // 2 + 10, center=True)
                draw_text(f"Coins Earned: {self.player.coins}", big_font, YELLOW, WIDTH // 2, HEIGHT // 2 + 55, center=True)
                draw_text("Press R", big_font, WHITE, WIDTH // 2, HEIGHT // 2 + 100, center=True)

        pygame.display.flip()

# =========================================================
# MAIN
# =========================================================
def main():
    game = Game()

    while True:
        clock.tick(FPS)
        game.handle_events()
        game.update()
        game.draw()

if __name__ == "__main__":
    main()