"""
Name: <Jalena Austin>
<Loops>.py

Problem: <This program is to use loops for different events to output arithmetics within
the loop and output the necessary amount to equate arithmetic evaluation.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Ashley Woods, Sam Austin>>
"""


def average():
    enter = eval(input('How many grades will you enter?'))
    average_acc = 0

    for i in range(enter):
        grade = eval(input('Enter grade'))
        average_acc = average_acc + grade

    average_grade = average_acc / enter

    print("Average is ", average_grade)


def tip_jar():
    tips = 0
    for i in range(1, 6):
        donate = eval(input('How much would you like to donate?'))
        tips = tips + donate

    print("Total tips: $", tips)


def newton():
    root = eval(input('What number do you want to square root? '))
    improve = eval(input('How many times should we improve the approximation? '))

    approximation = root

    for i in range(improve):
        approximation = (approximation + root / approximation) / 2

    print('The square root is approximately ', approximation)


def sequence():
    term = eval(input('How many terms would you like? '))
    terms_acc = 1

    for i in range(term):
        print(terms_acc, end=" ")
        terms_acc = terms_acc + 2 * (i % 2)


def pi():
    entered_n = eval(input('How many terms in the series? '))
    acc = 1

    for i in range(entered_n):
        num = i + (2.0 - (i % 2.0))

        den = i + (1.0 + (i % 2.0))

        acc = acc * (num / den)

    final = acc * 2
    print(final)


if __name__ == '__main__':
    pass
