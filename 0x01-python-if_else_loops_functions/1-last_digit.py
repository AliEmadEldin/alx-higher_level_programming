#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number>0:
    if abs(number)%10>5:
        print(f"last digit of {number} is {abs(number)%10} and is greater than 5")
    elif abs(number)%10<6 and abs(number)%10!=0:
        print(f"last digit of {number} is {abs(number)%10} and is less than 6 and not 0")
    else:
        print(f"last digit of {number} is {abs(number)%10}")
elif number<0:
    if abs(number)%10==0:
        print(f"last digit of {number} is {abs(number)%10}")
    elif abs(number)%10>0:
        print(f"last digit of {number} is -{abs(number)%10} and less than 6 and not 0")
