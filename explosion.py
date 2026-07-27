import turtle


class Explosion:

    def __init__(self):

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)

        self.active = False
        self.frame = 0
        self.x = 0
        self.y = 0

        self.colors = [
            "white",
            "yellow",
            "orange",
            "red"
        ]

    def start(self, x, y):

        self.x = x
        self.y = y

        self.frame = 0
        self.active = True

    def update(self):

        if not self.active:
            return

        self.pen.clear()

        if self.frame >= len(self.colors):

            self.pen.clear()
            self.active = False
            return

        self.pen.goto(self.x, self.y)

        size = 12 + self.frame * 8

        self.pen.dot(size, self.colors[self.frame])

        self.frame += 1
