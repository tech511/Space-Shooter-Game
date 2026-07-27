import turtle
import random

from settings import (
    WIDTH,
    HEIGHT,
    STAR_COUNT,
    STAR_MIN_SPEED,
    STAR_MAX_SPEED,
)


class StarField:

    def __init__(self, count=STAR_COUNT):

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)

        self.stars = []

        for _ in range(count):

            self.stars.append({
                "x": random.randint(-WIDTH // 2, WIDTH // 2),
                "y": random.randint(-HEIGHT // 2, HEIGHT // 2),
                "speed": random.randint(STAR_MIN_SPEED, STAR_MAX_SPEED)
            })

    def update(self):

        self.pen.clear()

        for star in self.stars:

            star["y"] -= star["speed"]

            if star["y"] < -HEIGHT // 2:
                star["y"] = HEIGHT // 2
                star["x"] = random.randint(-WIDTH // 2, WIDTH // 2)

            self.pen.goto(star["x"], star["y"])
            self.pen.dot(2, "white")
