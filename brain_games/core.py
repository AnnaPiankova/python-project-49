import prompt


def core_game(quiz, start_game):
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(start_game)
    while counter < 3:
        generated_question, correct_answer = quiz()
        #generated_question = get_question()
        #correct_answer = get_answer(function)
        print(f'Question:{generated_question}')
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            counter += 1
            print('Correct!')
        else:
            return print(f" {user_answer} is wrong answer ;(. Correct answer was {correct_answer}. \n Let's try again,{name}!")
    return print(f'Congratulations,{name}!')