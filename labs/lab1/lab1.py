"""
Name: <Jalena Austin>
<MonthlyInterest>.py

Problem: <Create a program that can accurately calculate inputs of annual interest rate, billing cycle and selected
billing cycle day, alongside net balance to calculate the monthly interest charge effectively.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def calc_ave_day_bal():
    annualrate = eval(input("What is your annual interest rate?  "))

    billday = eval(input("How many days is your billing cycle? "))

    netbal = eval(input("What was your previous or net balance? "))

    payamount = eval(input("What is your payment amount? "))

    payday = eval(input("What day of the cycle was your payment made? "))


    rate = annualrate / 100

    netbill = netbal * billday

    paybill = payamount * (billday - payday)

    bill = netbill - paybill

    average = bill / billday

    monthinterest = average * (rate / 12)
    interest = round(monthinterest, 2)

    print("Your monthly interest charge is: $",interest)

calc_ave_day_bal()