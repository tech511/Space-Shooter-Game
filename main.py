import turtle

from settings import *
from stars import StarField

# Create screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title(TITLE)

screen.tracer(0)

# Create stars
stars = StarField(180)

# Game Loop
while True:

    stars.update()

    screen.update()
