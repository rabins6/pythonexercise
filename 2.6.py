import random

three_digit_code = [random.randint(0, 9) for _ in range(3)]

four_digit_code = [random.randint(1, 6) for _ in range(4)]

print("3-Digit Code:", "".join(map(str, three_digit_code)))
print("4-Digit Code:", "".join(map(str, four_digit_code)))
