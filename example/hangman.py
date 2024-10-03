from the_hangman_wordlist import HangmanWordlist
from hangman_art import return_art

wordlist = HangmanWordlist()
word = wordlist.pull_word()

def return_letters(word_to_print):
    word_string = ""
    for char in word_to_print:
        if char in guessed_letters:
            word_string += char + " "
        else:
            word_string += "_ "
    return word_string

def check_win(word_to_check):
    if not "_" in return_letters(word_to_check):
        return True
    return False

def check_letter(guess_to_check , guessed_letters_list, correct_letters_list):
    if guess_to_check == word:
        for char in guess_to_check:
            check_letter(char, guessed_letters_list, correct_letters_list)
        return guessed_letters_list, correct_letters_list, check_win(guess_to_check)
    if len(guess_to_check) > 1:
        return guessed_letters_list, correct_letters_list, "too long"
    if guess_to_check in guessed_letters_list:
        return guessed_letters_list, correct_letters_list, "guessed"
    else:
        guessed_letters_list.append(guess_to_check)
        if guess_to_check in word:
            correct_letters_list.append(guess_to_check)
            return guessed_letters_list, correct_letters_list, True
        return guessed_letters_list, correct_letters_list, False

def return_guessed_correct_letters():
    guessed_string = ""
    correct_string = ""
    for char in guessed_letters:
        guessed_string += char + ", "
    for char in correct_letters:
        correct_string += char + ", "
    return guessed_string, correct_string

while True:
    lives = 10
    guessed_letters = []
    correct_letters = []
    while True:
        if check_win(word):
            print(f"You won, the word was \"{word}\"!")
            break
        if lives == 0:
            print(f"You lost, the word was \"{word}\"!")
            break
        print(return_art(lives))
        print(f"You have {lives} guesses left.")
        print(return_letters(word))
        print(f"Guessed: {return_guessed_correct_letters()[0]}\nCorrect: {return_guessed_correct_letters()[1]}")
        guess = input("Guess a letter: ").lower()
        guessed_letters, correct_letters, guess_in_word = check_letter(guess, guessed_letters, correct_letters)
        if not guess_in_word:
            lives -= 1
        if guess_in_word == "guessed":
            print(f"You have already guessed \"{guess}\"'.")
        if guess_in_word == "too long":
            print(f"\"{guess}\" is too long/incorrect.")
    play_again = input("Would you like to play again? (y/n) ").lower()
    match play_again:
        case "y":
            continue
        case _:
            break