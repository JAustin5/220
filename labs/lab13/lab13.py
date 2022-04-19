"""
Name: <Jalena Austin>
<ListsSearching>.py

Problem: <Selecting a capstone assignment (2) that will go through a file and count the specific amounts from the list
    within the file.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Isaiah Stapleton>
"""


def star_find(filename):
    # signal_count = 0
    fifth_indicator = 0
    pulse_ident = 0
    strength_acc = []
    f_name = open(filename, 'r')
    f_s_name = f_name.read().split(" ")

    i = 0

    while i < len(f_s_name):
        if 4000 <= int(f_s_name[i]) <= 5000 and fifth_indicator != 5:
            fifth_indicator += 1
            strength_acc.append(f_s_name[i])
        pulse_ident += 1
        # signal_count += 1
        i = i + 1

    print("Number of pulses found: {}".format(len(strength_acc)))
    print("Strength of each signal: {}".format(strength_acc))
    print("Number of signals found before fifth signal: {}".format(pulse_ident))

    f_name.close()
