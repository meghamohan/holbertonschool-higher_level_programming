#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
	lastDigit = number % 10
else:
	lastDigit = (abs(number) % 10) * -1
if lastDigit > 5:
	string = 'and is greater than 5'
elif lastDigit == 0:
	string = 'and is 0'
else:
	string = 'and is less than 6 and not 0'
print('Last digit of {:d} is {:d} {:s}'.format(number, lastDigit, string));
