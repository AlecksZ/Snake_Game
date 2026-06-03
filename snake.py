from turtle import Turtle , Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]

squares = []
screen = Screen()
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

        # Create squares
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

        # Key bindings
        screen.listen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkey(self.left, "Left")
        screen.onkey(self.right, "Right")

    def add_segment(self, position):
        square = Turtle()
        square.shape("square")
        square.color(random.choice(colors))
        square.penup()
        square.goto(position)

        self.squares.append(square)

    def reset_snake(self):
        for seg in self.squares:  # Previous "snake" will not disappear after a new one is generated so it will move out of the screen area
            seg.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.squares[-1].position())

    # Move function
    def move(self):

        # Move tail segments first
        for seg_num in range(len(self.squares) - 1, 0, -1):

            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()

            self.squares[seg_num].goto(new_x, new_y)

        # Move head forward
        self.squares[0].forward(20)

    # Direction methods
    def up(self):
        if self.head.heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)

