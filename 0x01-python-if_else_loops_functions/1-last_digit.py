#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = -(abs(number) % 10) if (number < 0) else number % 10
code = f"Last digit of {number:d} is {last_digit}"
if last_digit > 5:
    print(f"{code} and is greater than 5")
elif last_digit == 0:
    print(f"{code} and is 0")
elif last_digit < 6 and not 0:
    print(f"{code} and is less than 6 and not 0")
