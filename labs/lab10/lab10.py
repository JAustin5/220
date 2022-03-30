"""
Name: <Jalena Austin>
<Test_Lab10>.py

Problem: <Apply importing two different .py (Button and Door) to create a user interaction
    to making an infinite loop while still allowing users to exit loop when pressing the other function
    to leave the graphics window itself and close the program.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""
from graphics import *
from button import Button
from door import Door


def main():
    win = GraphWin("Test", 700, 700)

    button_rect = Rectangle(Point(250, 50), Point(500, 150))
    closing_button = Button(button_rect, 'Exit')
    closing_button.color_button('light grey')
    closing_button.draw(win)

    door_rect = Rectangle(Point(250, 200), Point(500, 700))
    selected_door = Door(door_rect, 'Closed')
    selected_door.color_door('dark red')
    selected_door.draw(win)

    user_click = win.getMouse()

    while not closing_button.is_clicked(user_click):
        if selected_door.is_clicked(user_click) and selected_door.get_label() == 'Open':
            selected_door.close('dark red', 'Closed')
        else:
            selected_door.open('white', 'Open')
        user_click = win.getMouse()
    win.close()
