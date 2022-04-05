"""
Name: <Jalena Austin>
<Door>.py

Problem: <Using tactics of defining a class to use multiple methods to create a door to work alongside button.py and
    lab10.py for user interaction.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""
from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        clicked_x = point.getX()
        clicked_y = point.getY()
        rect_x = self.shape.getP1()
        rect_y = self.shape.getP2()
        p1x = rect_x.getX()
        p1y = rect_x.getY()
        p2x = rect_y.getX()
        p2y = rect_y.getY()
        if p2x >= clicked_x >= p1x and p2y >= clicked_y >= p1y:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret
