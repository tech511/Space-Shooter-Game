import turtle

from settings import (
    WIDTH,
    HEIGHT,
    PLAYER_SPEED,
    CYAN,
)


class Player:

    def __init__(self):

        self.ship = turtle.Turtle()
        self.ship.penup()
        self.ship.speed(0)

        self.ship.shape("triangle")
        self.ship.color(CYAN)

        # Point upward
        self.ship.setheading(90)

        # Starting position
        self.ship.goto(0, -HEIGHT // 2 + 80)

    def move_left(self):

        x = self.ship.xcor() - PLAYER_SPEED

        limit = -WIDTH // 2 + 20

        if x < limit:
            x = limit

        self.ship.setx(x)

    def move_right(self):

        x = self.ship.xcor() + PLAYER_SPEED

        limit = WIDTH // 2 - 20

        if x > limit:
            x = limit

        self.ship.setx(x)

    def x(self):
        return self.ship.xcor()

    def y(self):
        return self.ship.ycor()
