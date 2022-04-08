"""
Name: <Jalena Austin>
<LoopsBool>.py

Problem: <Complete different methods to have a parameters with only the use of other syntax besides any for loops.>

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: <Brooke Duvall>
"""


def fibonacci(n):
    counter = 0
    if n < 1:
        return None
    previous = 1
    second_previous = 1

    while counter < n - 2:
        counter += 1
        second_previous_temp = previous
        previous += second_previous
        second_previous = second_previous_temp
    return previous


def double_investment(principle, rate):
    year_acc = 0
    current_prince = principle
    while current_prince < (2 * principle):
        year_acc += 1
        current_prince = current_prince * (1 + rate)
    return year_acc


def syracuse(n):
    acc_list = []
    take_n = n
    acc_list.append(int(take_n))
    while take_n != 1:
        if take_n % 2 == 0:
            take_n = take_n / 2
            acc_list.append(int(take_n))
        else:
            take_n = (take_n * 3) + 1
            acc_list.append(int(take_n))
    return acc_list


def goldbach(n):
    prime_list = []
    prime_counter = 1
    prime_list.append(2)
    while prime_counter < n:
        is_prime = True
        counter = 2
        while counter < prime_counter:
            if prime_counter % counter == 0:
                is_prime = False
            counter += 1
        if is_prime:
            prime_list.append(prime_counter)
        prime_counter += 2

    prime_list_two = []
    prime_index = 0
    while prime_index < len(prime_list):
        difference = n - prime_list[prime_index]
        counter = 0
        while counter < len(prime_list):
            if difference == prime_list[counter]:
                prime_list_two.append(prime_list[prime_index])
                prime_list_two.append(prime_list[counter])
                return prime_list_two
            counter += 1
        prime_index += 1


if __name__ == '__main__':
    pass
