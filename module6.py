import turtle
turtle.shape('turtle')
square=turtle.clone()
square.shape('square')
triangle=turtle.clone()
triangle.shape('triangle')
triangle.goto(100,200)
triangle.goto(0,0)
triangle.goto(300,350)
triangle.penup()
triangle.goto(100,200)
triangle.pendown()
triangle.goto(300,350)
square.penup()
square.goto(500,500)
square.stamp()
square.goto(0,0)
turtle.mainloop()


UP_AROWW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP
