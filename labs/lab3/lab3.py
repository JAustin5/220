"""
Name: <Jalena Austin>
<Traffic>.py

Problem: <How to use loop variables and nested loops to result in varying outputs that range from total
to averages that involve each variable.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>>
"""


def traffic():
    road = eval(input("How many roads were surveyed?"))
    vehicle_acc = 0

    for i in range(1, road+1):
        print("How many days was road", i, "surveyed?")
        day = eval(input(""))
        day_acc = 0

        for j in range(1, day+1):
            print("How many cars traveled on day", j, "?")
            vehicle = eval(input(""))
            day_acc = day_acc + vehicle
            vehicle_acc = vehicle_acc + vehicle

        print("Road", i, "average vehicles per day:", day_acc / day)

    print("Total number of vehicles traveled on all roads:", vehicle_acc)

    print("Average number of vehicles per road: ", vehicle_acc / road)
