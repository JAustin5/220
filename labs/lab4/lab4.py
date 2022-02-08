"""
Name: <Jalena Austin>
<GreetingCard>.py

Problem: <This program is to practice the use of the graphics import to create a visualization
of a Valentine's Day greeting card by the use of own considerations of how to output such visuals
of a heart, moving arrow, and greeting as a label.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Ashley Woods, Isiah Stapleton.>
"""
import time

from graphics import GraphWin, Text, Point, Line, Circle, Polygon


def greeting_card():
    win = GraphWin("Greeting Card", 400, 400)
    win.setBackground("pink")

    triangle = Polygon(Point(150, 150), Point(250, 150), Point(200, 275))
    triangle.setFill('maroon')
    triangle.setOutline('maroon')
    triangle.draw(win)

    left_circle = Circle(Point(175, 150), 24)
    left_circle.setFill('maroon')
    left_circle.setOutline('maroon')
    left_circle.draw(win)

    right_circle = left_circle.clone()
    right_circle.move(50, 0)
    right_circle.draw(win)

    label = Text(Point(200, 300), "Happy Valentine's Day!")
    label.setFace("courier")
    label.setSize(18)
    label.setTextColor("black")
    label.draw(win)

    a_arrow = Line(Point(70, 20), Point(80, 40))
    a_arrow.setArrow('last')
    a_arrow.draw(win)

    for i in range(50):
        a_arrow.move(5, 5)
        time.sleep(0.1)

    message = Text(Point(200, 375), "Click anywhere to close.")
    message.draw(win)

    win.getMouse()
    win.close()

greeting_card()