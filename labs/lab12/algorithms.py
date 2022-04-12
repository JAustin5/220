"""
Name: <your name goes here – first and last>
<Algorithms_LoopLists>.py

Problem: <Using the replacement of for loops to create methods with while loops, by reading through the line(s)
    of a list from a text file and outputting them into a list>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods, Isaish Stapleton>
"""


def read_data(filename):
    f_name = open(filename, 'r')
    line_read = f_name.readline()
    added_list = []
    while line_read:
        i = 0
        each_char = line_read.split()
        while i < len(each_char):
            added_list.append(int(each_char[i]))
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

