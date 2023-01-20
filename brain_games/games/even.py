from random import randint
import prompt


def is_even(number):
    return number % 2 == 0


def get_number():
    generated_number = randint(0, 100)
    return generated_number


def get_answer(generated_number):
    if is_even(generated_number) == True:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


start_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(start_game)
    while counter < 3:
        generated_number = get_number()
        correct_answer = get_answer(generated_number)
        print(f'Question:{generated_number}')
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            counter += 1
            print('Correct!')
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \n Let's try again,{name}!")
    return print(f'Congratulations,{name}!')
