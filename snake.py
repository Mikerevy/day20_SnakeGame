from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000,2000)

        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg - 1].xcor()
            y_position = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_position, y_position)
        self.snake_head.forward(20)


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)




#
#
# # Create a new segment - one square
# new_segment = Turtle()
# starting_position = [(0,0), (-20,0), (-40,0)]
# segments = []
#
# # Set up 3 squares behind ---
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("green")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
#     # For snake moving
# for seg in range(len(segments)-1, 0, -1):
#     x_position = segments[seg-1].xcor()
#     y_position = segments[seg-1].ycor()
#     segments[seg].goto(x_position, y_position)
#     # segments[seg].forward(20)
#     # segments[seg].left(90)
# segments[0].forward(20)
# segments[0].left(90)