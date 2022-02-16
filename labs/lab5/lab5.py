"""
Name: <Jalena Austin>
<Graphics>.py

Problem: <This program is to use strings and lists in various cases for algorithmic,
 drawing, and altering shape colors within various functions. This program
 also takes to making shapes overlap one another to create an image.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work, but I discussed it with:
<Ashley Woods, Arnold Aguila, Logan Segal>>
"""


from graphics import *
import math

def triange():
    win_width = 400
    win_height = 400
    win = GraphWin("Triangle Area & Perimeter", win_width, win_height)
    win.setBackground("white")

    message_1 = Text(Point(200, 200), "Click 3 times to create a triangle.")
    message_1.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    a_triangle = Polygon(p1, p2, p3)
    a_triangle.setFill("navy")
    a_triangle.setOutline("black")
    a_triangle.draw(win)

    side_1x = p2.getX() - p1.getX()
    side_1y = p2.getY() - p1.getY()
    length_a = math.sqrt((side_1x ** 2) + (side_1y ** 2))

    side_2x = p3.getX() - p2.getX()
    side_2y = p3.getY() - p2.getY()
    length_b = math.sqrt((side_2x ** 2) + (side_2y ** 2))

    side_3x = p1.getX() - p3.getX()
    side_3y = p1.getY() - p3.getY()
    length_c = math.sqrt((side_3x ** 2) + (side_3y ** 2))

    perimeter = (length_a + length_b + length_c) / 2

    s = perimeter

    area_acc = (s - length_a) * (s - length_b) * (s - length_c)
    area = math.sqrt(s * area_acc)

    perimeter_text = Point(200, 370)
    perimeter_message = Text(perimeter_text, "Perimeter: " + str(perimeter))
    perimeter_message.draw(win)

    area_dis = Point(200, 390)
    area_text = Text(area_dis, "Area: " + str(area))
    area_text.draw(win)

    close_dis = Point(200, 340)
    close_text = Text(close_dis, "Click again to close.")
    close_text.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_entry = Entry(Point(win_width / 2 + 50, win_height / 2 + 40), 10)
    red_entry.draw(win)
    red_text.setTextColor("red")

    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_entry = red_entry.clone()
    green_entry.move(0, 30)
    green_entry.draw(win)
    green_text.setTextColor("green")

    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_entry = red_entry.clone()
    blue_entry.move(0, 60)
    blue_entry.draw(win)
    blue_text.setTextColor("blue")

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red = red_entry.getText()
        r = eval(red_entry.getText())
        green = green_entry.getText()
        g = eval(green)
        blue = blue_entry.getText()
        b = eval(blue)
        shape.setFill(color_rgb(r, g, b))

    message = Text(Point(200, 100), "Click anywhere to close")
    message.draw(win)

    win.getMouse()
    win.close()


def process_string():
    string_int = input("Enter a string: ")

    first_char = string_int[0:1]
    print(first_char, end='\n')

    last_char = string_int[-1]
    print(last_char, end='\n')

    five_char = string_int[2:6]
    print(five_char, end='\n')

    first_and_last = first_char + last_char
    print(first_and_last, end='\n')

    first_three = string_int[0:4] * 10
    print(first_three, end='\n')

    each_char = []
    n = 1
    for index in range(0, len(string_int), n):
        each_char.append(string_int[index:index + n])
    print('\n'.join(each_char))

    num_string = len(string_int)
    print(num_string)


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] * 5
    print(x)

    x = values[2:5]
    print(x)

    x = [values[2], values[3], values[0]]
    print(x)

    x = [values[2], values[0], float(values[-1])]
    print(x)

    x = values[2] + values[0] + float(values[-1])
    print(x)

    x = len(values)
    print(x)


def another_series():
    n_elements = eval(input("How many terms to use? "))
    acc = 0

    for i in range(n_elements):
        value = 2 + (i % 3) * 2
        print(value, end=' ')
        acc = acc + value
    final = acc
    print('\n', 'sum = ', final)


def target():
    win_width = 400
    win_height = 400
    win = GraphWin("Target", win_width, win_height)
    win.setBackground("white")

    yellow_ring = Circle(Point(200, 200), 40)
    yellow_ring.setFill('yellow')
    yellow_ring.setOutline('black')

    red_ring = Circle(Point(200, 200), 75)
    red_ring.setFill('red')
    red_ring.setOutline('black')

    blue_ring = Circle(Point(200, 200), 110)
    blue_ring.setFill('blue')
    blue_ring.setOutline('black')

    black_ring = Circle(Point(200, 200), 145)
    black_ring.setFill('black')
    black_ring.setOutline('black')

    white_ring = Circle(Point(200, 200), 180)
    white_ring.setFill('white')
    white_ring.setOutline('black')

    white_ring.draw(win)
    black_ring.draw(win)
    blue_ring.draw(win)
    red_ring.draw(win)
    yellow_ring.draw(win)

    message = Text(Point(200, 390), "Click anywhere to close")
    message.draw(win)

    win.getMouse()
    win.close()
