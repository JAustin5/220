from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        win = self.window
        first_point = self.mouth.getP1()
        second_point = self.mouth.getP2()
        mid_point = Point((first_point.getX() + second_point.getX()) / 2, first_point.getY() + 50)
        line_one = Line(first_point, mid_point)
        line_one.draw(win)
        line_two = Line(second_point, mid_point)
        line_two.draw(win)

    def shock(self):
        win = self.window
        center_part = self.mouth.getCenter()
        shock_mouth = Circle(center_part, 25)
        self.mouth.undraw()
        shock_mouth.draw(win)

    def wink(self):
        win = self.window
        self.smile()
        center_wink = self.left_eye.getCenter()
        x_point = center_wink.getX()
        y_point = center_wink.getY()
        left_eye_wink = Line(Point(x_point - (0.15 * 25), y_point), Point(x_point + (0.15 * 25), y_point))
        self.left_eye.undraw()
        left_eye_wink.draw(win)
