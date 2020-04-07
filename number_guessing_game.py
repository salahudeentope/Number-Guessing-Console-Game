import random  # will be used to generate the random number


def right_answer():
    """
    A function to generate a random number between 1 and the maximum permitted number (n)
    based on the level selected by the player.

    :return: the right answer (answer), number of guesses allowed (guesses)
     and the maximum number (n)
    """
    print('Easy: guess a number between 1-10 with 6 guesses')
    print('Medium: Guess a number between 1-20 with 4 guesses')
    print('Hard: Guess a number between 1-50 with 3 guesses \n')
    level = input("Kindly input the level you want to play [easy, medium, hard]: ")

    while level.lower() not in ['easy', 'medium', 'hard']:  # to check that no invalid selection was made.
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
    """
    A function to take the players guess as an input and compare it to the right answer generated from the
    right_answer() function.

    :return: Prints that is wrong is the player inputs a number different from the right_answer,
    and prints "you got it right!" if the guess is same as the answer. I also prints "game over!" if
    the player runs out of guesses.
    """
    answer, guesses, n = right_answer()

    while guesses > 0:  # to check if the player still has guesses left.
        print(f"you have {guesses} guesses left")
        while True:
            try:  # to check if the player inputs something different from a number or a number out of range for the
                # level the player is playing.
                user_guess = int(input(f'Kindly input a guess between 1 - {n}: '))
            except ValueError:
                print(f'That is not a valid guess')
                # continue
            else:
                if user_guess < 1 or user_guess > n:
                    continue
                else:
                    break

        if user_guess != answer:  # if the player's guess is wrong.
            print("That was wrong!")
            guesses -= 1
            if guesses == 0:  # When the player is out of guesses.
                print('Game Over!')
            continue
        else:
            print("You got it right!")
            break


guessing_game()
