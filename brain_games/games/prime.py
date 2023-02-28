from random import randint


START_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for devider in range(2, number):
        if number % devider == 0:
            return False
    return True


def print_question():
    question = randint(2, 100)
    answer = "yes" if is_prime(question) else "no"
    return question, str(answer)
