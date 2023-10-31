#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = number % -10
else:
    rem = number % 10
if rem > 5:
    comment = "and is greater than 5"
elif rem == 0:
    comment = "and is 0"
else:
    comment = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, rem, comment))
