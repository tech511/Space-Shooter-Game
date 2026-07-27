import turtle

from settings import (
    BULLET_SPEED,
    YELLOW,
    HEIGHT,
)


class Bullet:

    def __init__(self):

        self.bullet = turtle.Turtle()
        self.bullet.hideturtle()
        self.bullet.penup()
        self.bullet.speed(0)

        self.bullet.shape("square")
        self.bullet.shapesize(stretch_wid=0.4, stretch_len=0.15)
        self.bullet.color(YELLOW)

        self.speed = BULLET_SPEED
        self.active = False

    def fire(self, x, y):

        if self.active:
            return

        self.active = True
        self.bullet.goto(x, y + 20)
        self.bullet.showturtle()

    def update(self):

        if not self.active:
            return

        self.bullet.sety(self.bullet.ycor() + self.speed)

        if self.bullet.ycor() > HEIGHT // 2 + 20:
            self.reset()

    def reset(self):

        self.active = False
        self.bullet.hideturtle()

    def x(self):
        return self.bullet.xcor()

    def y(self):
        return self.bullet.ycor()
