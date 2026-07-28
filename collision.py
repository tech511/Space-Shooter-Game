import math
import random

from settings import WIDTH, HEIGHT


def is_collision(x1, y1, x2, y2, distance=25):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < distance


def check_collisions(
    bullet,
    enemy,
    explosion,
    score,
    player,
    lives
):

    for e in enemy.get_enemies():

        t = e["turtle"]

        # -----------------------------
        # Bullet hits enemy
        # -----------------------------
        if bullet.active and is_collision(
            bullet.x(),
            bullet.y(),
            t.xcor(),
            t.ycor(),
            25
        ):

            # Explosion
            explosion.start(
                t.xcor(),
                t.ycor()
            )

            # Increase score
            score.add(10)

            # Reset bullet
            bullet.reset()

            # Respawn enemy
            t.goto(
                random.randint(-WIDTH // 2 + 30, WIDTH // 2 - 30),
                random.randint(HEIGHT // 2, HEIGHT + 300)
            )

            continue

        # -----------------------------
        # Enemy hits player
        # -----------------------------
        if is_collision(
            player.x(),
            player.y(),
            t.xcor(),
            t.ycor(),
            30
        ):

            # Player explosion
            explosion.start(
                player.x(),
                player.y()
            )

            # Lose one life
            lives.lose_life()

            # Respawn enemy
            t.goto(
                random.randint(-WIDTH // 2 + 30, WIDTH // 2 - 30),
                random.randint(HEIGHT // 2, HEIGHT + 300)
            )

            # Game Over
            if lives.game_over():
                return "game_over"

    return None
