import random

random_number = random.randint(1, 10)

def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    user_guess = get_user_guess()

    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number:", random_number)
        break

