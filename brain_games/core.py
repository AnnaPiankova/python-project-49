import prompt


def process_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.START_GAME)
    counter = 0
    while counter < 3:
        generated_question, correct = game.print_question()
        print(f'Question: {generated_question}')
        get = input("Your answer: ")
        if correct == get:
            counter += 1
            print('Correct!')
        else:
            print(
                f'''"{get}" is wrong answer ;(. Correct answer was "{correct}".
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
