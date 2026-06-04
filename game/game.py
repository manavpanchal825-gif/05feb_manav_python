import turtle
import random
import time

# Screen setup
wn = turtle.Screen()
wn.title("Catch The Star Game")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)   # turns off automatic screen update for animation

# Score
score = 0

# Player
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.shapesize(stretch_wid=1, stretch_len=3)
player.penup()
player.goto(0, -300)

# Falling object
star = turtle.Turtle()
star.shape("circle")
star.color("yellow")
star.penup()
star.goto(random.randint(-330, 330), 300)
star_speed = 3

# Score display
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-320, 310)
pen.write("Score: 0", font=("Arial", 16, "bold"))

# Game over display
game_text = turtle.Turtle()
game_text.hideturtle()
game_text.color("red")
game_text.penup()

# Move player left
def move_left():
    x = player.xcor()
    x -= 30
    if x < -320:
        x = -320
    player.setx(x)

# Move player right
def move_right():
    x = player.xcor()
    x += 30
    if x > 320:
        x = 320
    player.setx(x)

# Keyboard binding
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
lives = 3

while True:
    wn.update()
    time.sleep(0.01)

    # Move star downward
    y = star.ycor()
    y -= star_speed
    star.sety(y)

    # Collision with player
    if star.distance(player) < 40 and star.ycor() < -260:
        score += 1
        star_speed += 0.3   # speed increases = animation feels better
        star.goto(random.randint(-330, 330), 300)

        pen.clear()
        pen.write(f"Score: {score}", font=("Arial", 16, "bold"))

    # If star missed
    if star.ycor() < -340:
        lives -= 1
        star.goto(random.randint(-330, 330), 300)

        pen.clear()
        pen.write(f"Score: {score}   Lives: {lives}", font=("Arial", 16, "bold"))

    # Game over
    if lives <= 0:
        game_text.goto(0, 0)
        game_text.write("GAME OVER", align="center", font=("Arial", 28, "bold"))
        break

wn.mainloop()