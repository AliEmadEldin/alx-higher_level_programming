#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number%10 if number > 10 else number%-10
if number > 0:
    if n > 5:
        print(f"last digit of {number} is {n} and is greater than 5")
    elif n < 6 and n != 0:
        print(f"last digit of {number} is {n} and is less than 6 and not 0")
    else:
        print(f"last digit of {number} is {n}")
elif number < 0:
    if n < 0:
        print(f"last digit of {number} is {n} and is less than 6 and not 0")
    else:
        print(f"last digit of {number} is {n}")
else:
    print(f"last digit of {number} is {n}")