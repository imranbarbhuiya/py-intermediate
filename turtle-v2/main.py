import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "yellow")

# # squire
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# # dash line
# timmy.forward(10)
# timmy.penup()
# timmy.forward(10)
# timmy.pendown()
# timmy.forward(10)
# timmy.penup()

# # long dash line
# for _ in range(1, 15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # drawing a random shape
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
#
# for i in range(3, 11):
#     timmy.color(random.choice(colours))
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(360 / i)


# # drawing random walk
# generate random rbg color
turtle.colormode(255)


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(200):
    # timmy.color(random.choice(colours))
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(30)

screen = Screen()

screen.exitonclick()
