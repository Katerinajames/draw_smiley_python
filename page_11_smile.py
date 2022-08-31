import turtle

turtle.up()#εμφανίζεται το βελάκι 
turtle.goto(0,-100)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("pink")
turtle.circle(100)
turtle.end_fill() #central circle 


turtle.up()
turtle.goto(-67, -40)
turtle.setheading(-60)
turtle.width(6)
turtle.down()
turtle.circle(80, 120)  # draw smile
turtle.fillcolor("black")
for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)  # draw eyes
    turtle.end_fill()

turtle.hideturtle()
turtle.done()


turtle.Screen().exitonclick()
