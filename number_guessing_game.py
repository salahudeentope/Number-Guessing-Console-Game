import random


def right_answer():
    level = input("Kindly input the level you want to play [easy, medium, hard]: ")
    while level.lower() not in ['easy', 'medium', 'hard']:
        level = input("Kindly input a valid level selection [easy, medium, hard]: ")
    if level == 'easy':
        n = 10
    elif level == 'medium':
        n = 20
    else:
        n = 50
    return random.randint(1, n), level

def guessing_game():
    