from random import choice, randint


START_GAME = 'What is the result of the expression?'


def calculate(num_1, num_2, sign):
    match sign:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "*":
            return num_1 * num_2


def print_question():
    sign = choice(['+', '-', '*'])
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    answer = calculate(num1, num2, sign)
    question = f'{num1} {sign} {num2}'
    return question, str(answer)
