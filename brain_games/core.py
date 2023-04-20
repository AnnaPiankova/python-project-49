import prompt


def process_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    counter = 0
    while counter < 3:
        generated_question, correct_answer = game.generate()
        print(f'Question: {generated_question}')
        get_answer = prompt.string("Your answer: ")
        if correct_answer == get_answer:
            counter += 1
            print('Correct!')
        else:
            print(
                f'"{get_answer}" is wrong answer ;(.'
                f'Correct answer was "{correct_answer}".\n'
                f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
