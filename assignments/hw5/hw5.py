"""
Name: <Jalena Austin>
<ElementaryStrings>.py

Problem: <Using strings, lists, slicing, and indexing functions to be able to
 manipulate the user input and have different word/character orders, and
 calculating word averages for specific functions.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def name_reverse():
    name = input("What is your name (first and last): ").split()
    print(name[1] + ", " + name[0])


def company_name():
    domain_name = input("Enter a domain: ").split(".")
    print(domain_name[1])


def initials():
    num_students = int(input("How many students are in the class? "))

    for i in range(1, num_students + 1):
        student_number = i
        student_number = str(student_number)
        students_name = input("What is the students name " + student_number + "?").split()
        first_name = students_name[0]
        last_name = students_name[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        print(first_initial + last_initial)


def names():
    names_list = input('Enter a list of names (separated by a comma):').split(',')
    name = []

    for i in range(len(names_list)):
        person_name = names_list[i].split()
        first_name = person_name[0]
        last_name = person_name[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        full_initials = first_initial + last_initial
        name.append(full_initials)
    print(' '.join(name))


def thirds():
    num_sentence = int(input("Enter the number of sentence: "))
    list_acc = []

    for i in range(num_sentence):
        sentence = i + 1
        sentence = str(sentence)
        sentence_count = input("Enter sentence " + sentence + ":")
        list_acc.append(sentence_count[0::3])
    print("\n".join(list_acc))


def word_average():
    sentence = input('Enter a sentence: ')
    sum_acc = 0

    for i in sentence.split():
        character = len(i)
        sum_acc = sum_acc + character

    average = sum_acc / (len(sentence.split()))
    print(average)


def pig_latin():
    sentence = input('Enter a sentence to convert to pig latin: ').split()
    words = []

    for i in sentence:
        i = i[1:] + i[0:1] + 'ay'
        words.append(i.lower())
    print(' '.join(words))


if __name__ == '__main__':
    pass
