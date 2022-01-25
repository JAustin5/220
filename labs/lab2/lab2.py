"""
Name: <Jalena Austin>
<Means>.py

Problem: <This program is to ask for input(s) and complete different forms of
average calculations and output results to the user from their inputs.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""


def means():
    entered = eval(input("Enter the values to be entered: "))
    rms_acc = 0
    harmonic_acc = 0
    geometric_acc = 1

    for i in range(entered):
        value = eval(input("Enter value: "))
        rms_acc = rms_acc + value**2

        harmonic_acc = harmonic_acc + (1 / value)

        geometric_acc = geometric_acc * value

    rms_average = rms_acc / entered
    rms_average = rms_average**0.5

    harmonic_mean = entered / harmonic_acc

    geometric_mean = geometric_acc ** (1/entered)

    print("RMS average =", round(rms_average, 3))

    print("Harmonic mean =", round(harmonic_mean, 3))

    print("Geometric mean =", round(geometric_mean, 3))
