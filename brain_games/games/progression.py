from random import randint
from brain_games.core import core_game

start_game = 'What number is missing in the progression?'


def get_progression(start, step, length_of_prog):
    end = start + (length_of_prog * step)
    progression = list(range(start, end, step))
    return progression


def quiz():
    length_of_prog = 10
    miss_number_index = randint(1, length_of_prog - 1)
    step = randint(0, 10)
    start = randint(0, 10)
    progression = get_progression(start, step, length_of_prog)
    answer = progression.pop(miss_number_index)
    progression.insert(miss_number_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def run_game():
    core_game(quiz, start_game)