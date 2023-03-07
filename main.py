from turtle import Screen, Turtle
from scroller import Paddle
from ball import Ball
from scoreboad import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
spike = Ball()
scoreboard=Scoreboard()
game_is_on = True

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while game_is_on:
    time.sleep(spike.move_speed)
    screen.update()
    spike.move()

    # detect collision with wall
    if spike.ycor() > 280 or spike.ycor() < -280:
        spike.bounce_y()

    # collision with paddle
    if spike.distance(r_paddle) < 50 and spike.xcor() > 320 or spike.distance(l_paddle) < 50 and spike.xcor() < -320:
        spike.bounce_x()

    # Detect r paddle misses
    if spike.xcor() > 380:
        spike.reset_position()
        scoreboard.l_point()
    # Detect l paddle misses
    if spike.xcor() < -380:
        spike.reset_position()
        scoreboard.r_point()
screen.exitonclick()
