"""
Name: <Jalena Austin>
<Hangman>.py

Problem: <Creating a program with two different versions to play classic hangman game
 by use of various functions and input of these functions into two different play formats.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Brooke Duvall>
"""
from random import randint
from graphics import GraphWin, Circle, Point, Line, Text, Entry


def get_words(file_name):
    word_file = open(file_name, 'r')
    return word_file.readlines()


def get_random_word(words):
    return words[randint(0, len(words) - 1)].strip()


def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if letter == i:
            return True
    else:
        return False


def already_guessed(letter, guesses):
    for i in guesses:
        if letter == i:
            return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    blank = []
    for j in secret_word:
        blank.append("_")
    for i in range(len(guesses)):
        for letter in range(len(secret_word)):
            if guesses[i] == secret_word[letter]:
                blank[letter] = guesses[i]
    blanks = ' '.join(blank)
    return blanks


def won(guessed):
    for i in guessed:
        if i == '_':
            return False
    return True


def play_graphics(secret_word):
    win = GraphWin('Hangman', 650, 650)

    instruction_msg = Text(Point(225, 550), "Guess a letter: ")
    entry_box = Entry(Point(325, 550), 5)
    entry_box.draw(win)
    instruction_msg.draw(win)

    base_line = Line(Point(250, 450), Point(400, 450))
    base_line.draw(win)
    pole_line = Line(Point(360, 150), Point(360, 450))
    pole_line.draw(win)
    top_line = Line(Point(275, 150), Point(360, 150))
    top_line.draw(win)
    hang_line = Line(Point(275, 150), Point(275, 200))
    hang_line.draw(win)

    user_guesses = []
    tries = 6
    val_guess = True
    while (tries > 0) and not won(make_hidden_secret(secret_word, user_guesses)):
        while val_guess:
            win.getMouse()
            user_input = entry_box.getText()
            letters_guessed = Text(Point(317.5, 130), str(user_guesses) + user_input)
            letters_guessed.draw(win)
            word_blanks = Text(Point(317.5, 460), (make_hidden_secret(secret_word, user_guesses)))
            word_blanks.draw(win)
            if not already_guessed(user_input, user_guesses):
                word_bank = Text(Point(475, 130), user_guesses.append(user_input))
                word_bank.draw(win)
                val_guess = False
                if not letter_in_secret_word(user_input, secret_word) and tries == 6:
                    tries = tries - 1
                    face_circle = Circle(Point(275, 225), 27)
                    face_circle.draw(win)
                elif tries == 5:
                    body_line = Line(Point(275, 250), Point(275, 350))
                    body_line.draw(win)
                elif tries == 4:
                    right_arm = Line(Point(275, 270), Point(320, 300))
                    right_arm.draw(win)
                elif tries == 3:
                    left_arm = Line(Point(230, 300), Point(275, 270))
                    left_arm.draw(win)
                elif tries == 2:
                    right_leg = Line(Point(275, 350), Point(325, 400))
                    right_leg.draw(win)
                elif tries == 1:
                    left_leg = Line(Point(225, 400), Point(275, 350))
                    left_leg.draw(win)
        val_guess = True
    if won(make_hidden_secret(secret_word, user_guesses)):
        win_game = Text(Point(317.5, 100), 'Winner!')
        win_game.draw(win)
    else:
        lost_game = Text(Point(317.5, 130), 'Sorry, you did not guess the word. The secret word was ' + secret_word)
        lost_game.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    # secret_word = get_random_word(get_words('words.txt'))
    user_guesses = []
    tries = 6
    val_guess = True
    while (tries > 0) and not won(make_hidden_secret(secret_word, user_guesses)):
        while val_guess:
            print('\n' + 'Already guessed: ' + str(user_guesses))
            print('Guesses remaining: ' + str(tries))
            print(make_hidden_secret(secret_word, user_guesses))
            user_input = input('Guess a letter: ')
            if not already_guessed(user_input, user_guesses):
                val_guess = False
                user_guesses.append(user_input)
                if not letter_in_secret_word(user_input, secret_word):
                    tries = tries - 1
        val_guess = True
    if won(make_hidden_secret(secret_word, user_guesses)):
        print('\n' 'Winner!')
        print(secret_word)
    else:
        print('\n' + 'Sorry, you did not guess the word. ' '\n' + 'The secret word was ' + secret_word)


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
