import turtle

from settings import *
from stars import StarField
from player import Player

# Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title(TITLE)

screen.tracer(0)

# Objects
stars = StarField()
player = Player()

# Keyboard
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

# Game Loop
while True:

    stars.update()

    screen.update()
