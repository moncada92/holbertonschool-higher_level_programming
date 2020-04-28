#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = 0

if number > 0:
    lastnum = number % 10
else:
    lastnum = ((number * -1) % 10) * -1

print("Last digit of ", end="")
if lastnum > 5:
    print("{} is {} and is greater than 5".format(number, lastnum))
elif lastnum == 0:
    print("{} is {} and is 0".format(number, lastnum))
else:
    print("{} is {} and is less than 6 and not 0".format(number, lastnum))
