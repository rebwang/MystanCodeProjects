"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Create a variable for the discriminant, and use it to identify how many roots of the given numbers.
	use math.sqrt to calculate the exact root.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	# Create a variable for discriminant and use it to identify the amount of root
	discriminant = (b * b) - (4 * a * c)
	if discriminant > 0:
		print('Two roots: '+str((-b + math.sqrt(discriminant)) / (2 * a))+' , '+str((-b - math.sqrt(discriminant)) / (2 * a)))
	elif discriminant == 0:
		print('One root: '+str((-b + math.sqrt(discriminant)) / (2 * a)))
	else:
		print('No real roots')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
