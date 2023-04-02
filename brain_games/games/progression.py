from random import randint


TASK = 'What number is missing in the progression?'


def get_progression(start, step, length_of_prog):
    end = start + (length_of_prog * step)
    progression = list(range(start, end, step))
    return progression


def print_question():
    length_of_prog = 10
    miss_number_index = randint(1, length_of_prog - 1)
    step = randint(1, 10)
    start = randint(0, 10)
    progression = get_progression(start, step, length_of_prog)
    answer = progression.pop(miss_number_index)
    progression.insert(miss_number_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)
