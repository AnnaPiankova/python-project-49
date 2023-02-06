import prompt


def core_game(quiz, start_game):
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(start_game)
    while counter < 3:
        generated_question, correct = quiz()
        print(f'Question:{generated_question}')
        get = input("Your answer: ")
        if correct == get:
            counter += 1
            print('Correct!')
        else:
            return print(
                f'''"{get}" is wrong answer ;(. Correct answer was "{correct}".
Let's try again, {name}!''')
    return print(f'Congratulations, {name}!')
