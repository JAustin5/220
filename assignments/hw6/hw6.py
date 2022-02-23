"""
Name: <Jalena Austin>
<Strings>.py

Problem: <This program is to use various forms of string to create arguments and return values
    alongside modifying objects with differing parameters.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""
import math


def cash_converter():
    user_ent = eval(input("Enter an integer: "))
    cash = "That is ${:.2f}".format(user_ent)
    print(cash)


def encode():
    user_message = input('Enter a message: ')
    user_key = int(input('Enter a key: '))
    final_message = ''

    for i in range(len(user_message)):
        message_input = ord(user_message[i]) + user_key
        final_message += chr(message_input)

    print(final_message)


def sphere_area(radius):
    area_calc = float(4 * math.pi * (radius ** 2))
    return area_calc


def sphere_volume(radius):
    volume_calc = float((4 / 3) * math.pi * (radius ** 3))
    return volume_calc


def sum_n(number):
    for i in range(0, number + 1):
        n_value = int((number * (number + 1)) / 2)
        return n_value


def sum_n_cubes(number):
    for i in range(0, number + 1):
        cube_value = int(((number * (number + 1)) / 2) ** 2)
        return cube_value


def encode_better():
    user_message = input('Enter a message: ')
    user_key = input('Enter a key: ')
    final_message = ''

    for i in range(len(user_message)):
        message_input = ord(user_message[i]) - 65
        convert_key = ord(user_key[i % len(user_key)]) - 65
        new_code = message_input + convert_key
        shift_message = new_code % 58
        result_char = chr(shift_message + 65)
        final_message += result_char
    print(final_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
