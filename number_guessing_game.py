import random


def right_answer():
    print('Easy: guess a number between 1-10 with 6 guesses')
    print('Medium: Guess a number between 1-20 with 4 guesses')
    print('Hard: Guess a number between 1-50 with 3 guesses \n')
    level = input("Kindly input the level you want to play [easy, medium, hard]: ")

    while level.lower() not in ['easy', 'medium', 'hard']:
        level = input("Kindly input a valid level selection [easy, medium, hard]: ")
    if level.lower() == 'easy':
        n = 10
        guesses = 6
    elif level.lower() == 'medium':
        n = 20
        guesses = 4
    else:
        n = 50
        guesses = 3

    answer = random.randint(1, n)
    return answer, guesses, n


def guessing_game():
    answer, guesses, n = right_answer()

    while guesses > 0:
        print(f"you have {guesses} guesses left")
        while True:
            try:
                user_guess = int(input(f'Kindly input a guess between 1 - {n}: '))
            except ValueError:
                print(f'That is not a valid guess')
                continue
            else:
                break

        if user_guess != answer:
            print("That was wrong!")
            guesses -= 1
            if guesses == 0:
                print('Game Over!')
            continue
        else:
            print("You got it right!")
            break


guessing_game()
