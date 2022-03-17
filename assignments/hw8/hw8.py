"""
Name: <Jalena Austin>
<Conditionals>.py

Problem: <Creating various functions that use accumulations and/or conditional control statements
 to articulate the input(s) and output a true or false statement by the matters of the desired condition.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Brooke Duvall>
"""
from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = math.pow(nums[i], 2)


def sum_list(nums):
    nums_acc = 0
    for i in range(len(nums)):
        nums_acc = nums[i] + nums_acc
    return nums_acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    list_value = []
    for i in range(len(nums)):
        digit_split = nums[i].split(', ')
        to_numbers(digit_split)
        square_each(digit_split)
        value = sum_list(digit_split)
        list_value.append(value)
    return list_value


def starter(weight, wins):
    if (weight >= 150 and (weight < 160)) and (wins >= 5):
        return True
    elif (weight > 199) or (wins > 20):
        return True
    else:
        return False


def leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX() - circumference_point_two.getX()) ** 2 +
        (center_two.getY() - circumference_point_two.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("light green")
    circle_two.draw(win)

    overlap_message = Text(Point(5, 4), "The circles overlap.")
    overlap_not_message = Text(Point(5, 4), "The circles do not overlap.")
    closing_message = Text(Point(5, 3), "Click again to close.")

    if did_overlap(circle_one, circle_two):
        overlap_message.draw(win)
        closing_message.draw(win)
    else:
        overlap_not_message.draw(win)
        closing_message.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    squared_circles = math.sqrt(math.pow((circle_two.getCenter().getX() - circle_one.getCenter().getX()), 2)
                                + math.pow((circle_two.getCenter().getY() - circle_one.getCenter().getY()), 2))

    if squared_circles <= (circle_one.getRadius() + circle_two.getRadius()):
        return True
    else:
        return False


if __name__ == '__main__':
    pass
