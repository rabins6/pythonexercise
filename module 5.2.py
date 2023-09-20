numbers = []


while True:
    user_input = input("Enter a number (or press Enter to quit): ")


    if user_input == "":
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if len(numbers) < 5:
    print("You need to enter at least 5 numbers.")
else:

    numbers.sort(reverse=True)

   
    print("The five greatest numbers sorted in descending order are:")
    for i in range(5):
        print(numbers[i])