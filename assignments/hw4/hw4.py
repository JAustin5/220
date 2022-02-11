"""
Name: <Jalena Austin>
<Graphics>.py

Problem: <This program is to use different forms use of graphics to complete a visual and user
interactive program for each function alongside calculating area, perimeter, and radius for
a rectangle and/or circle. Alongside finding another form of approximating pi and creating
various copies of a square with the user interaction with the function.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work, but I discussed it with:<Ashley Woods, Arnold Aguila>>
"""
import math

from graphics import GraphWin, Point, Text, Circle, Rectangle


def squares():
    win = GraphWin("Clicks", 400, 400)

    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "Click to draw squares")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    win.setBackground("light gray")

    for i in range(5):
        click = win.getMouse()
        center = shape.getCenter()

        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)
        shape = Rectangle(Point(50, 50), Point(100, 100))
        shape.setFill('red')
        shape.setOutline('red')
        shape.draw(win)

    message = Text(Point(200, 200), "Click anywhere to close")
    message.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)

    win.setBackground('light grey')

    p1 = win.getMouse()
    p2 = win.getMouse()

    a_rectangle = Rectangle(p1, p2)
    a_rectangle.setFill("dark green")
    a_rectangle.setOutline("black")
    a_rectangle.draw(win)

    width = p2.getX() - p1.getX()
    length = p2.getY() - p1.getY()
    area = width * length
    perimeter = 2 * area

    perimeter_text = Point(200, 370)
    perimeter_message = Text(perimeter_text, "Perimeter: " + str(perimeter))
    perimeter_message.draw(win)

    area_dis = Point(200, 390)
    area_text = Text(area_dis, "Area: " + str(area))
    area_text.draw(win)

    message = Text(Point(200, 200), "Click anywhere to close.")
    message.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()

    d = math.sqrt(((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2))

    user_circle = Circle(p1, d)
    user_circle.setFill("light blue")
    user_circle.setOutline('black')
    user_circle.draw(win)

    d_text = Point(200, 375)
    d_message = Text(d_text, "Radius: " + str(d))
    d_message.draw(win)

    message = Text(Point(200, 200), "Click anywhere to close.")
    message.draw(win)

    win.getMouse()
    win.close()


def pi2():
    terms = eval(input("Enter the number of terms to sum: "))
    den = 1
    num = 4
    total = 0

    for i in range(terms):
        total = total + (num / den)

        den = den + 2
        num = num * - 1

    accuracy = math.pi - total

    print("pi approximation: ", total)
    print('accuracy: ', accuracy)


if __name__ == '__main__':
    pass
