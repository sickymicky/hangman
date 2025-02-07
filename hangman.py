import random, os

from wordlist import words
from check_spaces import check_for_spaces

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}


def display_man(wrong_guesses):
    print("*" * stars)

    for line in hangman_art[wrong_guesses]:
        print(line)

    print("*" * stars)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


stars = 20


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)

    check_for_spaces(answer, hint)

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    os.system("clear")
    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("\nEnter a letter: ").lower()
        os.system("clear")

        if len(guess) != 1 or not guess.isalpha():
            print(f"Guessed letters: {guessed_letters}")
            print("Invalid input!")
            continue

        if guess in guessed_letters:
            print(f"Guessed letters: {guessed_letters}")
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)
        print(f"Guessed letters: {guessed_letters}")

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
                    guessed_letters.add(guess)
        else:
            wrong_guesses += 1

            print(f"{guess} not in word!")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()
