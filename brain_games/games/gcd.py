from random import randint
from brain_games.core import core_game


start_game = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    divisor = min(num1, num2)
    while divisor > 0:
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
        divisor -= 1


def quiz():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    question = f'{num1} {num2}'
    answer = get_gcd(num1, num2)
    return question, str(answer)


def run_game():
    core_game(quiz, start_game)
