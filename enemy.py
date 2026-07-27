import turtle
import random

from settings import (
    WIDTH,
    HEIGHT,
    ENEMY_COUNT,
    ENEMY_MIN_SPEED,
    ENEMY_MAX_SPEED,
    RED,
)


class Enemy:

    def __init__(self):

        self.enemies = []

        for _ in range(ENEMY_COUNT):

            enemy = turtle.Turtle()
            enemy.penup()
            enemy.speed(0)
            enemy.shape("circle")
            enemy.color(RED)

            enemy.goto(
                random.randint(-WIDTH//2 + 30, WIDTH//2 - 30),
                random.randint(HEIGHT//2, HEIGHT + 500)
            )

            self.enemies.append({
                "turtle": enemy,
                "speed": random.uniform(
                    ENEMY_MIN_SPEED,
                    ENEMY_MAX_SPEED
                )
            })

    def update(self):

        for enemy in self.enemies:

            e = enemy["turtle"]

            e.sety(e.ycor() - enemy["speed"])

            if e.ycor() < -HEIGHT//2 - 40:

                e.goto(
                    random.randint(-WIDTH//2 + 30, WIDTH//2 - 30),
                    random.randint(HEIGHT//2, HEIGHT + 300)
                )

                enemy["speed"] = random.uniform(
                    ENEMY_MIN_SPEED,
                    ENEMY_MAX_SPEED
                )

    def get_enemies(self):
        return self.enemies
