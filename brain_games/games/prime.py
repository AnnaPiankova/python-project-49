from random import randint
from brain_games.core import core_game


start_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for devider in range(2, number):
        if number % devider == 0:
            return False
    return True


def quiz():
    question = randint(2, 100)
    answer = "'yes'" if is_prime(question) else "'no'"
    return question, answer


def run_game():
    core_game(quiz, start_game)
