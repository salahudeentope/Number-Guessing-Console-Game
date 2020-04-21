import random  # will be used to generate the random number


def right_answer():
    """
    A function to generate a random number between 1 and the maximum permitted number (n)
    based on the level selected by the player.

    :return: the right answer (answer), number of guesses allowed (guesses)
     and the maximum number (n)
    """
    print("These are the available levels!")
    print('Easy: guess a number between 1-10 with 6 guesses')
    print('Medium: Guess a number between 1-20 with 4 guesses')
    print('Hard: Guess a number between 1-50 with 3 guesses \n')
    level = input("Kindly input the level you want to play [easy [E], medium[M], hard[H]]: ")

    while level.lower() not in ['easy', 'e', 'medium', 'm', 'hard', "h"]:  # to check that no invalid selection was
        # made.
        level = input("Kindly input a valid level selection [easy [E], medium [M], hard[H]]: ")
    if level.lower() in ['easy', "e"]:
        n = 10
        guesses = 6
    elif level.lower() in ['medium', "m"]:
        n = 20
        guesses = 4
    else:
        n = 50
        guesses = 3

    answer = random.randint(1, n)
    return answer, guesses, n


def guessing_game():
    print("Welcome to this fun guessing game!")
    print()
    """
    A function to take the players guess as an input and compare it to the right answer generated from the
    right_answer() function.

    :return: Prints "That was wrong!" if the player inputs a number different from the right_answer,
    and prints "you got it right!" if the guess is same as the answer. It also prints "game over!" if
    the player runs out of guesses.
    """
    continue_game = "yes"
    while continue_game == 'yes':
        answer, guesses, n = right_answer()

        while guesses > 0:  # to check if the player still has guesses left.
            print(f"you have {guesses} guesses left")
            while True:
                try:  # to check if the player inputs something different from a number or a number out of range for the
                    # level the player is playing.
                    user_guess = int(input(f'Kindly input a guess between 1 - {n}: '))
                except ValueError:
                    print(f'That is not a valid guess')
                else:
                    try: # to ensure that the player only inputs a number in the specified range.
                        while user_guess < 1 or user_guess > n:
                            user_guess = int(input(f'please enter a guess that is greater than one and less than or '
                                                   f'equal to {n} '))
                    except ValueError:
                        print('that is not a valid guess')
                    else:
                        break

            if user_guess != answer:  # if the player's guess is wrong.
                print("That was wrong!")
                guesses -= 1

                if guesses == 0:  # When the player is out of guesses.
                    print('Game Over!')
                    print(f'Thank you for playing, the answer is {answer}')
                continue
            else:
                print(f"You got it right! the answer is indeed {answer}")
                break

        # To ask the player if they want to play another gain after finishing a game.
        continue_game = input("Do you want to play again? [yes/no] ").lower()
        while continue_game not in ['yes', 'no']:
            continue_game = input('kindly input a valid selection [yes/no]')
        if continue_game == 'yes':
            print()
            continue
        else:
            print("Thank you for playing!")


guessing_game()
