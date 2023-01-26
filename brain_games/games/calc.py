from random import choice, randint
from brain_games.core import core_game

start_game = 'What is the result of the expression?'
sign = choice(['+', '-', '*'])


def get_expression(num_1, num_2, sign):
    if sign == '+':
        result = num_1 + num_2
    elif sign == '-':
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    return result


def quiz():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    answer = get_expression(num1, num2, sign)
    question = f'{num1}{sign}{num2}'
    return question, str(answer)


def run_game():
    core_game(quiz, start_game)
