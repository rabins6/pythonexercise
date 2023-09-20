def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:

        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


try:
    user_input = int(input("Enter an integer: "))

    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")