"""
Name: <Jalena Austin>
<Functions>.py

Problem: <Will be able to create functions to not only write functions, but open
 to opening text files, while allowing the user to read and/or write within these text files
 that are opened.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Brooke Duvall>
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    my_file = open(in_file_name, 'r')
    word_vale = 0
    new_file = open(out_file_name, 'w')

    for line in my_file:
        for word in line.split():
            word_vale = word_vale + 1
            new_file.write(str(word_vale) + " " + word + "\n")

    my_file.close()
    new_file.close()


def hourly_wages(in_file_name, out_file_name):
    start_file = open(in_file_name, 'r')
    new_file = open(out_file_name, 'w')

    for line in start_file:
        line_var = line.split()
        for i in range(len(line_var)):
            wage_var = eval(line_var[2])
            hour_var = eval(line_var[3])
            sum_pay = (wage_var * hour_var) + (1.65 * hour_var)
        new_file.write(line_var[0] + ' ' + line_var[1] + ' ' + "{:.2f}".format(sum_pay) + '\n')

    start_file.close()
    new_file.close()


def calc_check_sum(isbn):
    user_isbn = isbn.replace('-', '')
    total = 0

    for i in range(10):
        cur_val = user_isbn[::-1]
        user_index = eval(cur_val[i])
        total = total + (user_index * (i + 1))
    return total


def send_message(file_name, friend_name):
    start_file = open(file_name, 'r')
    reading_file = file_name.read()
    new_file = open(friend_name + '.txt', 'a')
    new_file.write(reading_file)

    start_file.close()
    new_file.close()


def send_safe_message(file_name, friend_name, key):
    start_file = open(file_name, 'r')
    file = start_file.read()
    file_info = file.split('\n')
    new_friend = open(friend_name + '.txt', 'a')

    for i in range(len(file_info)):
        encoded = encode(file_info[i], key)
        new_friend.write(encoded + '\n')

    start_file.close()
    new_friend.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    open_file = open(file_name, 'r')
    message = open_file.read()
    key_file = open(pad_file_name, 'r')
    key = key_file.read()
    message_count = message.split()

    for i in message_count:
        encode_better(i, key, friend_name + '.txt')

    open_file.close()
    key_file.close()


if __name__ == '__main__':
    pass
