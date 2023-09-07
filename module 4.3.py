smallest = None
largest = None

while True:
    user_input = input("Enter a number (or an empty string to quit): ")


    if user_input == "":
        break

    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number


if smallest is not None and largest is not None:
    print(f"The smallest number entered is: {smallest}")
    print(f"The largest number entered is: {largest}")
else:
    print("No valid numbers were entered.")