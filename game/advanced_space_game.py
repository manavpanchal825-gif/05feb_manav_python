import turtle
import random
import time
import math

# =========================================================
# SCREEN SETUP
# =========================================================
wn = turtle.Screen()
wn.title("Advanced Space Fighter")
wn.bgcolor("black")
wn.setup(width=1000, height=750)
wn.tracer(0)

# =========================================================
# GAME STATE
# =========================================================
GAME_STATE = "menu"   # menu, playing, paused, gameover
score = 0
level = 1
health = 100
lives = 3
boss_active = False
boss_health = 0
boss_spawn_score = 25

# Object lists
player_bullets = []
enemy_bullets = []
enemies = []
stars = []
explosions = []
powerups = []

# =========================================================
# BORDER
# =========================================================
LEFT_BOUND = -470
RIGHT_BOUND = 470
TOP_BOUND = 330
BOTTOM_BOUND = -330

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(LEFT_BOUND, BOTTOM_BOUND)
border.pendown()
border.pensize(3)
for _ in range(2):
    border.forward(RIGHT_BOUND - LEFT_BOUND)
    border.left(90)
    border.forward(TOP_BOUND - BOTTOM_BOUND)
    border.left(90)

# =========================================================
# TEXT TURTLES
# =========================================================
hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.color("white")
hud.goto(-455, 345)

message = turtle.Turtle()
message.hideturtle()
message.penup()
message.color("cyan")

boss_bar_pen = turtle.Turtle()
boss_bar_pen.hideturtle()
boss_bar_pen.penup()

# =========================================================
# PLAYER
# =========================================================
player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -260)
player.shapesize(stretch_wid=1.2, stretch_len=1.4)

player_speed = 25
player_shoot_cooldown = 0
player_flash = 0

# =========================================================
# BOSS
# =========================================================
boss = turtle.Turtle()
boss.shape("square")
boss.color("red")
boss.penup()
boss.shapesize(stretch_wid=2.5, stretch_len=5)
boss.hideturtle()
boss.dx = 4
boss.fire_delay = 0

# =========================================================
# FUNCTIONS - DISPLAY
# =========================================================
def update_hud():
    hud.clear()
    hud.write(
        f"Score: {score}   Level: {level}   Health: {health}   Lives: {lives}",
        font=("Arial", 16, "bold")
    )

def show_message(text, color="cyan", y=0, size=24):
    message.clear()
    message.goto(0, y)
    message.color(color)
    message.write(text, align="center", font=("Arial", size, "bold"))

def clear_message():
    message.clear()

def draw_boss_bar():
    boss_bar_pen.clear()
    if boss_active:
        max_width = 300
        width = max(0, (boss_health / 50) * max_width)

        boss_bar_pen.goto(-150, 300)
        boss_bar_pen.color("white")
        boss_bar_pen.pendown()
        boss_bar_pen.pensize(2)
        for _ in range(2):
            boss_bar_pen.forward(300)
            boss_bar_pen.left(90)
            boss_bar_pen.forward(20)
            boss_bar_pen.left(90)
        boss_bar_pen.penup()

        boss_bar_pen.goto(-150, 300)
        boss_bar_pen.color("red")
        boss_bar_pen.begin_fill()
        boss_bar_pen.pendown()
        for _ in range(2):
            boss_bar_pen.forward(width)
            boss_bar_pen.left(90)
            boss_bar_pen.forward(20)
            boss_bar_pen.left(90)
        boss_bar_pen.end_fill()
        boss_bar_pen.penup()

        boss_bar_pen.goto(0, 325)
        boss_bar_pen.color("white")
        boss_bar_pen.write("BOSS HEALTH", align="center", font=("Arial", 12, "bold"))

# =========================================================
# FUNCTIONS - STARS
# =========================================================
def create_stars():
    for _ in range(50):
        s = turtle.Turtle()
        s.shape("circle")
        s.color("white")
        s.penup()
        s.shapesize(stretch_wid=0.1, stretch_len=0.1)
        s.goto(random.randint(LEFT_BOUND + 10, RIGHT_BOUND - 10),
               random.randint(BOTTOM_BOUND + 10, TOP_BOUND - 10))
        s.speed_value = random.uniform(1, 4)
        stars.append(s)

def move_stars():
    for s in stars:
        y = s.ycor() - s.speed_value
        if y < BOTTOM_BOUND:
            y = TOP_BOUND
            s.setx(random.randint(LEFT_BOUND + 10, RIGHT_BOUND - 10))
        s.sety(y)

# =========================================================
# FUNCTIONS - PLAYER MOVEMENT
# =========================================================
def move_left():
    if GAME_STATE != "playing":
        return
    x = player.xcor() - player_speed
    if x < LEFT_BOUND + 20:
        x = LEFT_BOUND + 20
    player.setx(x)

def move_right():
    if GAME_STATE != "playing":
        return
    x = player.xcor() + player_speed
    if x > RIGHT_BOUND - 20:
        x = RIGHT_BOUND - 20
    player.setx(x)

def move_up():
    if GAME_STATE != "playing":
        return
    y = player.ycor() + player_speed
    if y > TOP_BOUND - 30:
        y = TOP_BOUND - 30
    player.sety(y)

def move_down():
    if GAME_STATE != "playing":
        return
    y = player.ycor() - player_speed
    if y < BOTTOM_BOUND + 20:
        y = BOTTOM_BOUND + 20
    player.sety(y)

# =========================================================
# FUNCTIONS - BULLETS
# =========================================================
def shoot_laser():
    global player_shoot_cooldown
    if GAME_STATE != "playing":
        return
    if player_shoot_cooldown > 0:
        return

    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("yellow")
    bullet.penup()
    bullet.shapesize(stretch_wid=0.2, stretch_len=1.2)
    bullet.setheading(90)
    bullet.goto(player.xcor(), player.ycor() + 15)
    bullet.speed_value = 18
    player_bullets.append(bullet)

    player_shoot_cooldown = 8

def create_enemy_bullet(x, y, color="orange", speed=8):
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color(color)
    bullet.penup()
    bullet.shapesize(stretch_wid=0.2, stretch_len=0.8)
    bullet.goto(x, y)
    bullet.speed_value = speed
    enemy_bullets.append(bullet)

# =========================================================
# FUNCTIONS - ENEMIES
# =========================================================
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color(random.choice(["red", "orange", "magenta"]))
    enemy.penup()
    enemy.goto(random.randint(LEFT_BOUND + 30, RIGHT_BOUND - 30),
               random.randint(150, TOP_BOUND - 20))
    enemy.dx = random.choice([-3, -2, 2, 3])
    enemy.dy = random.randint(2, 4) + (level * 0.25)
    enemy.fire_rate = random.randint(60, 140)
    enemy.fire_count = random.randint(0, 80)
    enemies.append(enemy)

def create_enemy_wave():
    count = min(4 + level, 10)
    for _ in range(count):
        create_enemy()

def move_enemies():
    global health, lives, GAME_STATE

    for enemy in enemies[:]:
        enemy.setx(enemy.xcor() + enemy.dx)
        enemy.sety(enemy.ycor() - enemy.dy * 0.2)

        if enemy.xcor() >= RIGHT_BOUND - 20 or enemy.xcor() <= LEFT_BOUND + 20:
            enemy.dx *= -1

        enemy.fire_count += 1
        if enemy.fire_count >= enemy.fire_rate:
            create_enemy_bullet(enemy.xcor(), enemy.ycor() - 10, "orange", 7 + level * 0.2)
            enemy.fire_count = 0

        if enemy.ycor() < BOTTOM_BOUND:
            enemy.goto(random.randint(LEFT_BOUND + 30, RIGHT_BOUND - 30), TOP_BOUND - 20)

        if enemy.distance(player) < 25:
            create_explosion(enemy.xcor(), enemy.ycor())
            enemy.goto(random.randint(LEFT_BOUND + 30, RIGHT_BOUND - 30), TOP_BOUND - 20)
            damage_player(20)

# =========================================================
# FUNCTIONS - BOSS
# =========================================================
def spawn_boss():
    global boss_active, boss_health
    boss_active = True
    boss_health = 50
    boss.goto(0, 250)
    boss.showturtle()
    boss.dx = 5
    boss.fire_delay = 0

def move_boss():
    global boss_active, score, level, boss_spawn_score

    if not boss_active:
        return

    boss.setx(boss.xcor() + boss.dx)

    if boss.xcor() > RIGHT_BOUND - 90 or boss.xcor() < LEFT_BOUND + 90:
        boss.dx *= -1

    boss.fire_delay += 1
    if boss.fire_delay >= 18:
        create_enemy_bullet(boss.xcor() - 40, boss.ycor() - 20, "red", 9)
        create_enemy_bullet(boss.xcor(), boss.ycor() - 20, "red", 10)
        create_enemy_bullet(boss.xcor() + 40, boss.ycor() - 20, "red", 9)
        boss.fire_delay = 0

def boss_hit():
    global boss_health, boss_active, score, level, boss_spawn_score

    boss_health -= 1
    create_explosion(boss.xcor(), boss.ycor())

    if boss_health <= 0:
        create_big_explosion(boss.xcor(), boss.ycor())
        boss.hideturtle()
        boss_active = False
        score += 20
        level += 1
        boss_spawn_score += 35
        create_enemy_wave()
        update_hud()

# =========================================================
# FUNCTIONS - POWERUP
# =========================================================
def create_powerup():
    power = turtle.Turtle()
    power.shape("square")
    power.color("green")
    power.penup()
    power.shapesize(stretch_wid=0.8, stretch_len=0.8)
    power.goto(random.randint(LEFT_BOUND + 20, RIGHT_BOUND - 20), TOP_BOUND - 30)
    power.dy = 3
    powerups.append(power)

def move_powerups():
    global health
    for power in powerups[:]:
        power.sety(power.ycor() - power.dy)

        if power.ycor() < BOTTOM_BOUND:
            power.hideturtle()
            powerups.remove(power)
        elif power.distance(player) < 20:
            health += 20
            if health > 100:
                health = 100
            power.hideturtle()
            powerups.remove(power)
            update_hud()

# =========================================================
# FUNCTIONS - EXPLOSION
# =========================================================
def create_explosion(x, y):
    e = turtle.Turtle()
    e.shape("circle")
    e.color("yellow")
    e.penup()
    e.goto(x, y)
    e.frame = 0
    explosions.append(e)

def create_big_explosion(x, y):
    for _ in range(6):
        ex = x + random.randint(-30, 30)
        ey = y + random.randint(-20, 20)
        create_explosion(ex, ey)

def animate_explosions():
    for e in explosions[:]:
        e.frame += 1

        if e.frame == 1:
            e.color("yellow")
            e.shapesize(1.2, 1.2)
        elif e.frame == 2:
            e.color("orange")
            e.shapesize(1.8, 1.8)
        elif e.frame == 3:
            e.color("red")
            e.shapesize(2.2, 2.2)
        elif e.frame == 4:
            e.color("gray")
            e.shapesize(1.5, 1.5)
        else:
            e.hideturtle()
            explosions.remove(e)

# =========================================================
# FUNCTIONS - DAMAGE / LIFE
# =========================================================
def damage_player(amount):
    global health, lives, GAME_STATE, player_flash

    health -= amount
    player_flash = 10

    if health <= 0:
        lives -= 1
        if lives > 0:
            health = 100
            player.goto(0, -260)
        else:
            game_over()

    update_hud()

def handle_player_flash():
    global player_flash
    if player_flash > 0:
        if player_flash % 2 == 0:
            player.color("white")
        else:
            player.color("cyan")
        player_flash -= 1
    else:
        player.color("cyan")

# =========================================================
# FUNCTIONS - COLLISIONS
# =========================================================
def move_player_bullets():
    global score, level

    for bullet in player_bullets[:]:
        bullet.sety(bullet.ycor() + bullet.speed_value)

        if bullet.ycor() > TOP_BOUND:
            bullet.hideturtle()
            player_bullets.remove(bullet)
            continue

        # Hit normal enemies
        for enemy in enemies[:]:
            if bullet.distance(enemy) < 20:
                create_explosion(enemy.xcor(), enemy.ycor())
                enemy.goto(random.randint(LEFT_BOUND + 30, RIGHT_BOUND - 30), TOP_BOUND - 20)
                bullet.hideturtle()
                if bullet in player_bullets:
                    player_bullets.remove(bullet)
                score += 1
                update_hud()

                if random.randint(1, 12) == 1:
                    create_powerup()
                break

        # Hit boss
        if boss_active and bullet in player_bullets:
            if bullet.distance(boss) < 55:
                bullet.hideturtle()
                player_bullets.remove(bullet)
                boss_hit()

def move_enemy_bullets():
    for bullet in enemy_bullets[:]:
        bullet.sety(bullet.ycor() - bullet.speed_value)

        if bullet.ycor() < BOTTOM_BOUND:
            bullet.hideturtle()
            enemy_bullets.remove(bullet)
        elif bullet.distance(player) < 18:
            create_explosion(player.xcor(), player.ycor())
            bullet.hideturtle()
            enemy_bullets.remove(bullet)
            damage_player(10)

# =========================================================
# FUNCTIONS - GAME CONTROL
# =========================================================
def start_game():
    global GAME_STATE
    if GAME_STATE == "menu":
        GAME_STATE = "playing"
        clear_message()

def toggle_pause():
    global GAME_STATE
    if GAME_STATE == "playing":
        GAME_STATE = "paused"
        show_message("PAUSED\nPress P to Resume", "yellow", y=0, size=28)
    elif GAME_STATE == "paused":
        GAME_STATE = "playing"
        clear_message()

def game_over():
    global GAME_STATE
    GAME_STATE = "gameover"
    show_message("GAME OVER\nPress R to Restart", "red", y=0, size=28)

def reset_game():
    global score, level, health, lives, boss_active, boss_health, boss_spawn_score
    global GAME_STATE, player_shoot_cooldown, player_flash

    score = 0
    level = 1
    health = 100
    lives = 3
    boss_active = False
    boss_health = 0
    boss_spawn_score = 25
    player_shoot_cooldown = 0
    player_flash = 0

    player.goto(0, -260)
    player.color("cyan")
    boss.hideturtle()

    for obj_list in [player_bullets, enemy_bullets, enemies, explosions, powerups]:
        for obj in obj_list:
            obj.hideturtle()
        obj_list.clear()

    create_enemy_wave()
    update_hud()
    boss_bar_pen.clear()
    GAME_STATE = "menu"
    show_message("ADVANCED SPACE FIGHTER\n\nPress ENTER to Start\nArrow Keys = Move\nSpace = Shoot\nP = Pause", "cyan", y=40, size=24)

# =========================================================
# KEYBOARD
# =========================================================
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(shoot_laser, "space")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(start_game, "Return")
wn.onkeypress(reset_game, "r")

# =========================================================
# INITIALIZE
# =========================================================
create_stars()
create_enemy_wave()
update_hud()
show_message("ADVANCED SPACE FIGHTER\n\nPress ENTER to Start\nArrow Keys = Move\nSpace = Shoot\nP = Pause", "cyan", y=40, size=24)

# =========================================================
# MAIN LOOP
# =========================================================
while True:
    wn.update()
    time.sleep(0.02)

    move_stars()
    animate_explosions()
    handle_player_flash()

    if player_shoot_cooldown > 0:
        player_shoot_cooldown -= 1

    if GAME_STATE == "playing":
        move_player_bullets()
        move_enemy_bullets()
        move_enemies()
        move_powerups()

        if boss_active:
            move_boss()
        else:
            if score >= boss_spawn_score:
                spawn_boss()

        draw_boss_bar()
    else:
        draw_boss_bar()