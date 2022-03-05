"""
Name: <Jalena Austin>
<Functions>.py

Problem: <Will be able to create functions to not only write functions, but open
 to opening text files, while allowing the user to read and/or write within these text files
 that are opened.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Brooke Duvall, Sam Austin, Ashley Woods>
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    my_file = open(in_file_name, 'r')
    word_vale = 0
    new_file = open(out_file_name, 'w')

    for line in my_file:
        for word in line.split():
            word_vale = word_vale + 1
            print(str(word_vale) + " " + word, file=new_file)

    my_file.close()
    new_file.close()

    print(new_file)


def hourly_wages(in_file_name, out_file_name):
    start_file = open(in_file_name, 'r')
    new_file = open(out_file_name, 'w')

    for line in start_file:
        line_var = line.split()
        for i in range(len(line_var)):
            wage_var = eval(line_var[2])
            hour_var = eval(line_var[3])
            sum_pay = (wage_var * hour_var) + (1.65 * hour_var)
        print(line_var[0] + ' ' + line_var[1] + ' ' + "{:.2f}".format(sum_pay), file=new_file)

    start_file.close()
    new_file.close()

    print(out_file_name)


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
    first_file = start_file.readlines()
    new_file = open(friend_name + '.txt', 'w')

    for line in first_file:
        first_var = line.split()
        for word in first_var:
            word += word
        print(line.replace('\n', ''), file=new_file)

    start_file.close()
    new_file.close()

    print(friend_name)


def send_safe_message(file_name, friend_name, key):
    start_file = open(file_name, 'r')
    file_read = start_file.read().split()
    new_friend = open(friend_name + '.txt', 'w')

    for i in range(len(file_read)):
        encoded = encode(file_read[i], key)
        print(encoded.replace('\n', ''), file=new_friend)

    start_file.close()
    new_friend.close()

    print(friend_name)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    open_file = open(file_name, 'r')
    open_var = open_file.read()
    encry_file = open(pad_file_name, 'r')
    encry_enter = encry_file.read()
    friend_n_fil = open(friend_name + '.txt', 'w')

    encoded = encode_better(open_var, encry_enter)
    print(encoded, file=friend_n_fil)

    open_file.close()
    encry_file.close()
    friend_n_fil.close()

    print(friend_name)


if __name__ == '__main__':
    pass
