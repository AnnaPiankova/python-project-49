from random import randint


START_GAME = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    divisor = min(num1, num2)
    while divisor > 0:
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
        divisor -= 1


def print_question():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    question = f'{num1} {num2}'
    answer = get_gcd(num1, num2)
    return question, str(answer)
