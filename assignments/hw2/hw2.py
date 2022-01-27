"""
Name: <Jalena Austin>
<Arithmetic>.py

Problem: <This program is applying loops and range to calculate different arithmetics forms
to solve exponents, area, alongside principles of multiplication with it.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    bound_acc = 0
    for i in range(bound_acc, upper_bound + 1, 3):
        bound_acc = i + bound_acc

    print("Sum of threes is", bound_acc)


sum_of_threes()


def multiplication_table():
    for rows in range(1, 11):
        for columns in range(1, 11):
            print(rows * columns, end="\t")
        print()


multiplication_table()


def triangle_area():
    side_a = float(input("Enter side a length: "))
    side_b = float(input("Enter side b length: "))
    side_c = float(input("Enter side c length: "))

    perimeter = (side_a + side_b + side_c) / 2

    s_1 = (perimeter - side_a) * (perimeter - side_b) * (perimeter - side_c)

    s_2 = perimeter * s_1

    area = math.sqrt(s_2)

    print("The area is:", area)


triangle_area()


def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))

    range_acc = 0

    for i in range(lower_range, upper_range + 1):
        range_acc = range_acc + i*i

    print(range_acc)


sum_squares()


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))

    final = 1

    for i in range(exponent):
        final = final * base

    print(base, "^", exponent, "=", final)


power()

if __name__ == '__main__':
    pass
