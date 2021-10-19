# need file pool in future
import random

print("H A N G M A N")


def game_start():
    answers = ['python', 'java', 'kotlin', 'javascript']
    right_answer = random.choice(answers)
    dashes = list('-' * len(right_answer))
    attempt = 0
    user_guess_letters = []

    while attempt < 8:
        print()
        string = "".join(dashes)
        print(string)

        if '-' not in dashes:
            print(f'You guessed the word {right_answer}!')
            print("You survived!")
            break

        user_guess_letter = input('Input a letter:')

        if user_guess_letter in user_guess_letters:
            print("You've already guessed this letter")

        elif len(user_guess_letter) > 1:
            print("You should input a single letter")

        elif user_guess_letter == user_guess_letter.upper():
            print('Please enter a lowercase English letter')

        elif user_guess_letter in right_answer and user_guess_letter.lower():
            user_guess_letters.append(user_guess_letter)
            for i in range(len(right_answer)):
                if user_guess_letter == right_answer[i]:
                    dashes[i] = user_guess_letter
        else:
            user_guess_letters.append(user_guess_letter)
            print("That letter doesn't appear in the word")
            attempt += 1

    if '-' in dashes:
        print("You lost!")


def menu():
    user_choise = input('Type "play" to play the game, "exit" to quit: ')
    if user_choise == "play":
        game_start()
    elif user_choise == "exit":
        exit()
    else:
        menu()
menu()