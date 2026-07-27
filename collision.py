import math
import random

from settings import WIDTH, HEIGHT


def is_collision(x1, y1, x2, y2, distance=25):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < distance


def check_collisions(bullet, enemy, explosion):

    for e in enemy.get_enemies():

        t = e["turtle"]

        if bullet.active and is_collision(
            bullet.x(),
            bullet.y(),
            t.xcor(),
            t.ycor()
        ):

            # Start explosion
            explosion.start(t.xcor(), t.ycor())

            # Hide bullet
            bullet.reset()

            # Respawn enemy
            t.goto(
                random.randint(-WIDTH//2 + 30, WIDTH//2 - 30),
                random.randint(HEIGHT//2, HEIGHT + 300)
            )

            return True

    return False
