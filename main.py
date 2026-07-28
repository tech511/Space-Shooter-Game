import turtle

from settings import *

from stars import StarField
from player import Player
from bullet import Bullet
from enemy import Enemy
from explosion import Explosion
from collision import check_collisions
from score import Score
from lives import Lives

# =====================================
# Screen
# =====================================

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title(TITLE)

screen.tracer(0)

# =====================================
# Game Objects
# =====================================

stars = StarField()

player = Player()

bullet = Bullet()

enemy = Enemy()

explosion = Explosion()

score = Score()

lives = Lives()

# =====================================
# Keyboard
# =====================================

screen.listen()

screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


def shoot():
    bullet.fire(player.x(), player.y())


screen.onkeypress(shoot, "space")

# =====================================
# Game Loop
# =====================================

game_running = True

while game_running:

    stars.update()

    bullet.update()

    enemy.update()

    explosion.update()

    result = check_collisions(
        bullet,
        enemy,
        explosion,
        score,
        player,
        lives
    )

    if result == "game_over":
        game_running = False

    screen.update()

# =====================================
# Game Over Screen
# =====================================

game_over = turtle.Turtle()

game_over.hideturtle()

game_over.penup()

game_over.color("red")

game_over.write(
    "GAME OVER",
    align="center",
    font=("Arial", 36, "bold")
)

screen.mainloop()
