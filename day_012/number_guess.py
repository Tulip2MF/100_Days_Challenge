from art_guess import art
from random import randint
from check_number_function import number_check


while True:
    print(art)
    random_number = randint(1, 100)
    print(random_number)
    level = input("select the level. 'H' for hard & 'E' for easy: ").lower()
    if level == "h":
        attempt = 5
    elif level == "e":
        attempt = 10
    else:
        print("Invalid entry. Gate set to Easy level")
        attempt = 10
    for life in range(attempt):
        guess_number = int(input("Guess the number between 1 and 100"))
        end_game = number_check(guess_number,random_number,attempt,life)
        if end_game == "y":
            break
    should_continue = input("Press 'N' to exit or any other key to continue").lower()
    if should_continue == "n":
        break

