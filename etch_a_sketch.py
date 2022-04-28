from turtle import Turtle, Screen

starfire = Turtle()
screen = Screen()


def move_forwards():
    starfire.forward(10)


def move_back():
    starfire.back(10)


def move_left():
    starfire.left(10)


def move_right():
    starfire.right(10)


def clear_reset():
    starfire.clear()
    starfire.penup()
    starfire.home()
    starfire.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_reset)


screen.exitonclick()
