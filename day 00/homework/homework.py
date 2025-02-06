from turtle import *

# square
speed(40)
width(5)
color("orange")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

# door
begin_fill()
forward(70)
color("red")
left(90)
forward(90)
right(90)

forward(50)
right(90)
forward(90)
end_fill()

# roof
penup()
goto(200, 200)
pendown()

color("gray")
begin_fill()
forward(5)
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# windows
penup()
goto(135, 135)
pendown()

color("green")
begin_fill()
left(120)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
goto(50, 130)
pendown()

left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()

exitonclick()