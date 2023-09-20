import random

def roll_dice(sides):
    rolls = 0
    while True:
        result = random.randint(1, sides)
        rolls += 1
        print(f"You rolled a {result} on a {sides}-sided dice.")
        if result == sides:
            break
    return rolls

def main():
    max_sides = int(input("Enter the maximum number of sides on the dice: "))
    rolls = roll_dice(max_sides)
    print(f"It took {rolls} rolls to get the maximum number on the {max_sides}-sided dice.")

if __name__ == "__main__":
    main()
