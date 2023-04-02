import prompt


def process_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    counter = 0
    while counter < 3:
        generated_question, correct = game.print_question()
        print(f'Question: {generated_question}')
        recive = input("Your answer: ")
        if correct == recive:
            counter += 1
            print('Correct!')
        else:
            print(
                f'"{recive}" is wrong answer ;(.'
                f'Correct answer was "{correct}".\n'
                f"Let's try again, {name}!"
                )
            return
    print(f'Congratulations, {name}!')
