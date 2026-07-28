import turtle

from settings import WIDTH, HEIGHT, WHITE, PLAYER_LIVES


class Lives:

    def __init__(self):

        self.lives = PLAYER_LIVES

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.color(WHITE)

        self.pen.goto(WIDTH // 2 - 160, HEIGHT // 2 - 40)

        self.draw()

    def draw(self):

        self.pen.clear()

        self.pen.write(
            f"Lives : {self.lives}",
            align="left",
            font=("Arial", 18, "bold")
        )

    def lose_life(self):

        if self.lives > 0:
            self.lives -= 1

        self.draw()

    def game_over(self):

        return self.lives <= 0
