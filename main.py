import turtle

from settings import *
from stars import StarField
from player import Player
from bullet import Bullet
from enemy import Enemy
from explosion import Explosion
from collision import check_collisions
from score import Score

# Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title(TITLE)

screen.tracer(0)

# Objects
stars = StarField()
player = Player()
bullet = Bullet()
enemy = Enemy()
explosion = Explosion()
score = Score()

# Keyboard
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

# Game Loops 
while True:

    stars.update()

    bullet.update()

    enemy.update()

    explosion.update()

    check_collisions(
        bullet,
        enemy,
        explosion,
        score
    )

    screen.update()
