import random
lower_bound = 1
max_bound = 10
max_attempts = 10
my_num = random.randint(lower_bound, max_bound)
def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {max_bound}: "))
            if lower_bound <= guess <= max_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def check_guess(guess, my_num):
    if guess == my_num:
        return "Correct"
    elif guess < my_num:
        return "Your input is Too low"
    else:
        return "Your input is Too high"
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, my_num)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {max_bound} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {my_num}.")
if __name__ == "__main__":
    print("Welcome to this Number Guessing Game!")
    play_game()