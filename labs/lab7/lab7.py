"""
Name: <Jalena Austin>
<lab7>.py

Problem: <Create various programs that use different decision statements and using random
 generating forms to show through different outputs such as Boolean or none.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Ashley Woods, Isaiah Stapleton>
"""
import math
from random import randint
from graphics import *


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball_2):
    ball_center = ball.getCenter()
    ball_rad = ball.getRadius()

    ball_2_center = ball_2.getCenter()
    ball_2_rad = ball_2.getRadius()

    distance_x = (ball_center.getX() - ball_2_center.getX()) ** 2
    distance_y = (ball_center.getY() - ball_2_center.getY()) ** 2
    distance_value = math.sqrt(distance_x + distance_y)

    rad_value = ball_rad + ball_2_rad

    if distance_value <= rad_value:
        return True
    else:
        return False


def hit_vertical(ball, win):
    ball_center = ball.getCenter().getY()
    ball_rad = ball.getRadius()

    win_span = win.getHeight()

    if ball_center <= ball_rad or ball_center >= win_span - ball_rad:
        return True
    else:
        return False


def hit_horizontal(ball, win):
    ball_center = ball.getCenter().getX()
    ball_rad = ball.getRadius()

    win_span = win.getWidth()

    if ball_center <= ball_rad or ball_center <= win_span - ball_rad:
        return True
    else:
        return False


def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))


def bumper():
    win = GraphWin("Bumper (Lab 7)", 500, 500)

    circle_1 = Circle(Point(randint(10, 480), randint(10, 480)), 20)
    circle_2 = Circle(Point(randint(10, 480), randint(10, 480)), 20)

    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    circle_1.draw(win)
    circle_2.draw(win)

    circle_1_x = get_random(10)
    circle_1_y = get_random(8)
    circle_2_x = get_random(10)
    circle_2_y = get_random(8)

    while not win.checkMouse():
        time.sleep(.1)
        circle_1.move(circle_1_x, circle_1_y)
        circle_2.move(circle_2_x, circle_2_y)
        if did_collide(circle_1, circle_2):
            circle_1_x = -circle_1_x
            circle_1_y = -circle_1_y
            circle_2_x = -circle_2_x
            circle_2_y = -circle_2_y
        if hit_horizontal(circle_1, win):
            circle_1_x = -circle_1_x
        if hit_horizontal(circle_2, win):
            circle_2_x = -circle_2_x
        if hit_vertical(circle_1, win):
            circle_1_y = -circle_1_y
        if hit_vertical(circle_2, win):
            circle_2_y = -circle_2_y

    win.close()


bumper()