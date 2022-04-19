"""
Name: <Jalena Austin

Problem: <Using the replacement of for loops to create methods with while loops, by reading through the line(s)
    of a list from a text file and outputting them into a list>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods, Isaiah Stapleton>
"""
import math
from graphics import *


def read_data(filename):
    f_name = open(filename, 'r')
    line_read = f_name.readline()
    added_list = []
    while line_read:
        i = 0
        each_char = line_read.split()
        while i < len(each_char):
            added_list.append(eval(each_char[i]))
            i += 1
        line_read = f_name.readline()
    f_name.close()
    return added_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True

        i += 1

    return False


def selection_sort(values):
    for i in range(1, len(values)):
        sel_sorting = values[i]
        mini = i
        while (mini > 0) and (values[mini - 1] > sel_sorting):
            values[mini] = values[mini - 1]
            mini = mini - 1
        values[mini] = sel_sorting


def calc_area(rect):
    rect_width = abs(rect.getP2().getY() - rect.getP1().getY())
    rect_length = abs(rect.getP2().getX() - rect.getP1().getX())
    angle_area = rect_width * rect_length
    return angle_area


def rect_sort(rectangles):
    for i in range(1, len(rectangles)):
        angle_rect = rectangles[i]
        next_angle = i
        while calc_area(rectangles[next_angle - 1]) > calc_area(angle_rect):
            rectangles[next_angle] = rectangles[next_angle - 1]
            next_angle = next_angle - 1
        rectangles[next_angle] = angle_rect
