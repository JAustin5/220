"""
Name: <Jalena Austin>
<LoopsLists>.py

Problem: <To create various functions that replace the general use of for loops to those of a while loop.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""
from random import randint


def find_and_remove_first(list, value):
    name = str('Jalena')
    if value in list:
        index = list.index(value)
        list.remove(value)
        list.insert(index, name)


def good_input():
    user_input = eval(input('Enter a number within the range 1 - 10'))
    while not (user_input <= 10 and user_input >= 1):
        if user_input >= 11:
            print('This input is too high! Try again. ')
            user_input = eval(input('Enter a number within the range 1 - 10'))
        elif user_input <= 0:
            print('This input is too low! Try again. ')
            user_input = eval(input('Enter a number within the range 1 - 10'))
        else:
            return user_input


def num_digits():
    digit_pos = int(input('Enter a positive integer: '))
    while not digit_pos <= 0:
        count = 0
        while not digit_pos <= 0:
            digit_pos = digit_pos // 10
            count += 1
        print('The amount of digits is:', count)
        digit_pos = int(input('Enter a positive integer: '))


def hi_lo_game():
    guesses = 7
    random_choice = randint(1, 100)
    users_choice = eval(input("Enter a positive integer between 1 to 100. Good luck! "))
    while not (users_choice == random_choice) and (guesses != 1):
        if users_choice >= random_choice:
            guesses -= 1
            print('Too high!')
            print('You have ' + str(guesses) + ' guesses left. ')
            users_choice = eval(input("Enter a positive integer between 1 to 100. "))
        elif users_choice <= random_choice:
            guesses -= 1
            print('Too low!')
            print('You have ' + str(guesses) + ' guesses left. ')
            users_choice = eval(input("Enter a positive integer between 1 to 100. "))
    if (users_choice == random_choice) and (guesses != 0):
        print('You win!')
        print('You win in ' + str(guesses) + 'guesses.')
    else:
        print('Sorry, you lose. The number was ' + str(random_choice))


