"""
Name: <Jalena Austin>
<Vigenere>.py

Problem: <Creating a program that uses entry of the user to output a new message
    by going through each character of the message and shifting them each by the provided
    keyword by the user input.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods, Isaiah Stapleton>
"""
from graphics import *


def vigenere():
    win = GraphWin('Vigenere', 600, 400)
    win.setBackground('white')

    message_code_pt = Point(150, 90)
    message_code = Text(message_code_pt, "Message to code")
    message_code.draw(win)
    message_entry = Entry(Point(400, 90), 30)
    message_entry.draw(win)

    key_enter_pt = Point(150, 130)
    key_enter = Text(key_enter_pt, "Enter Keyword")
    key_enter.draw(win)
    key_entry = Entry(Point(400, 130), 30)
    key_entry.draw(win)

    rectangle_box = Rectangle(Point(250, 150), Point(350, 200))
    rectangle_box.draw(win)
    rec_text_pt = rectangle_box.getCenter()
    rec_text = Text(rec_text_pt, "Encode")
    rec_text.draw(win)

    win.getMouse()

    message_char = message_entry.getText().upper().replace(' ', '')
    key_text = key_entry.getText().upper().replace(' ', '')
    resulting_message = ''

    for i in range(len(message_char)):
        message_input = ord(message_char[i]) - 65
        conv_mess_code = ord(key_text[i % len(key_text)]) - 65
        new_code = message_input + conv_mess_code
        shift_mess = new_code % 26
        resulting_char = chr(shift_mess + 65)
        resulting_message += resulting_char

    rectangle_box.undraw()
    rec_text.undraw()

    result_pt = Point(300, 240)
    message_code = Text(result_pt, "Resulting Message")
    message_code.draw(win)
    answer_pt = Point(300, 260)
    answer_show = Text(answer_pt, resulting_message)
    answer_show.draw(win)

    close_mess_pt = Point(300, 380)
    close_mess = Text(close_mess_pt, "Click Anywhere to Close Window")
    close_mess.draw(win)

    win.getMouse()
    win.close()


vigenere()