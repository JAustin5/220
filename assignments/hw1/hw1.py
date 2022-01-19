"""
Name: <Jalena Austin>
<GettingStarted>.py

Problem: <This program is used to evaluate different inputs of various kinds to
    accurately calculate simple conversions or to have various amounts be calculated
    to one form of measurements or converting one form of measurement to another.
    This program takes into account different forms of inputs to get a particular
    output of the desired form by producing outputs and doing specific arithmetic.>

Certification of Authenticity: <I certify that this assignment is entirely my own work.>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


calc_rec_area()

print()


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


calc_volume()

print()


def shooting_percentage():
    total = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = (made / total) * 100
    print("Shooting percentage:", percentage, "%")


shooting_percentage()

print()


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    perlbs = pounds * 10.50
    shipping = pounds * 0.86
    total = perlbs + shipping + 1.50
    print("You're total is: $", total)


coffee()

print()


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")


kilometers_to_miles()


if __name__ == '__main__':
    pass
