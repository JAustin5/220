"""
Name: <Jalena Austin>
<three_door_game>.py

Problem: <Use created functions from previous lab to create a game for user interaction to select and count
    the amount of times a user gets the correct and wrong door by random generation of what is the secret door.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""
from lab10.door import Door
from lab10.button import Button
from random import randint
from graphics import *


def three_door_game():
    win = GraphWin('Three Door Game', 700, 700)
    win.setBackground('light blue4')

    secret_door_msg = Text(Point(350, 150), "I have a secret door. ")
    secret_door_msg.draw(win)

    begin_msg = Text(Point(350, 600), "Click to guess which is the secret door! ")
    begin_msg.draw(win)

    wins_txt = Text(Point(100, 45), "Wins")
    wins_txt.draw(win)
    loss_txt = Text(Point(170, 45), 'Losses')
    loss_txt.draw(win)

    count_box_win = Rectangle(Point(65, 60), Point(135, 110))
    count_box_win.draw(win)

    count_box_loss = Rectangle(Point(135, 60), Point(205, 110))
    count_box_loss.draw(win)

    exit_button = Button(Rectangle(Point(500, 40), Point(650, 110)), 'Exit')
    exit_button.draw(win)

    wins_acc = 0
    loss_acc = 0
    win_count = Text(Point(100, 85), wins_acc)
    win_count.draw(win)
    loss_count = Text(Point(170, 85), loss_acc)
    loss_count.draw(win)

    door_1 = Door(Rectangle(Point(5, 200), Point(200, 500)), 'Door 1')
    door_1.color_door('brown')
    door_1.draw(win)
    door_2 = Door(Rectangle(Point(250, 200), Point(450, 500)), 'Door 2')
    door_2.color_door('brown')
    door_2.draw(win)
    door_3 = Door(Rectangle(Point(500, 200), Point(695, 500)), 'Door 3')
    door_3.color_door('brown')
    door_3.draw(win)

    random_door_selected = randint(1, 3)
    if random_door_selected == 1:
        door_1.set_secret(True)
    elif random_door_selected == 2:
        door_2.set_secret(True)
    elif random_door_selected == 3:
        door_3.set_secret(True)

    winner_msg = Text(Point(350, 150), "You win! ")
    loss_msg = Text(Point(350, 150), "Sorry, Incorrect! ")
    play_again_txt = Text(Point(350, 600), "Click anywhere to play again. ")

    click = win.getMouse()
    while not exit_button.is_clicked(click):
        secret_door_msg.undraw()
        begin_msg.undraw()
        if door_1.is_clicked(click) and door_1.is_secret():
            wins_acc += 1
            win_count.setText(wins_acc)
            door_1.color_door('green')
            winner_msg.draw(win)
        elif door_2.is_clicked(click) and door_2.is_secret():
            wins_acc += 1
            win_count.setText(wins_acc)
            door_2.color_door('green')
            winner_msg.draw(win)
        elif door_3.is_clicked(click) and door_3.is_secret():
            wins_acc += 1
            win_count.setText(wins_acc)
            door_3.color_door('green')
            winner_msg.draw(win)
        else:
            if door_1.is_clicked(click):
                loss_acc += 1
                loss_count.setText(loss_acc)
                door_1.color_door('red')
                loss_msg.draw(win)
            elif door_2.is_clicked(click):
                loss_acc += 1
                loss_count.setText(loss_acc)
                door_2.color_door('red')
                loss_msg.draw(win)
            elif door_3.is_clicked(click):
                loss_acc += 1
                loss_count.setText(loss_acc)
                door_3.color_door('red')
                loss_msg.draw(win)

            if door_1.is_secret():
                door_1.color_door('green')
            elif door_2.is_secret():
                door_2.color_door('green')
            elif door_3.is_secret():
                door_3.color_door('green')

        play_again_txt.draw(win)
        click = win.getMouse()
        if exit_button.is_clicked(click):
            win.close()
        else:
            winner_msg.undraw()
            loss_msg.undraw()
            play_again_txt.undraw()

            door_1.set_secret(False)
            door_2.set_secret(False)
            door_3.set_secret(False)

            door_1.color_door('brown')
            door_2.color_door('brown')
            door_3.color_door('brown')

            random_door_selected = randint(1, 3)
            if random_door_selected == 1:
                door_1.set_secret(True)
            elif random_door_selected == 2:
                door_2.set_secret(True)
            elif random_door_selected == 3:
                door_3.set_secret(True)

            begin_msg.draw(win)
            secret_door_msg.draw(win)
            click = win.getMouse()
    win.close()

