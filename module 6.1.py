import random

def roll_dice():
    return random.randint(1, 6)

def main():
    rolls = 0
    result = None

    while result != 6:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")

    print(f"Congratulations! It took {rolls} rolls to get a 6.")

if __name__ == "__main__":
    main()