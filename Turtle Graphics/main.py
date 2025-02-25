from turtle import Turtle
from turtle import Screen
from paddle import Paddle

new_screen = Screen()
new_screen.setup(width = 800, height = 600)
new_screen.bgcolor("black")
new_screen.title("pong")
new_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

new_screen.listen()
new_screen.onkey(r_paddle.go_up, "Up")
new_screen.onkey(r_paddle.go_down, "Down")
new_screen.onkey(l_paddle.go_up, "w")
new_screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    new_screen.update()


new_screen.exitonclick()