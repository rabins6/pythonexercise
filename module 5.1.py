import random

def main():
    try:
        num_dice = int(input("How many dice do you want to roll? "))
        if num_dice <= 0:
            print("Please enter a positive number of dice to roll.")
            return

        total_sum = 0
        for _ in range(num_dice):
           
            roll = random.randint(1, 6)
            print(f"Rolled: {roll}")
            total_sum += roll

        print(f"Sum of the numbers rolled: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter a valid number of dice.")

if __name__ == "__main__":
    main()