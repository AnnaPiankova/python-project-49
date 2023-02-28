from random import randint


START_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def print_question():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, str(answer)
