"""
File: extension1_factioral.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	First need to check if the given number is 0 or 1. The factorial for these two numbers is 1.
	Create a variable for factorial, and if the given number is > 1,
	calculate the factorial by using the given number & factorial.
	"""
	print('Welcome to stanCode factorial master!')
	data = int(input('Give me a number, and I will list the answer of factorial: '))
	if data == EXIT:
		print('------ See ya! ------')
	else:
		if data == 0:
			print('Answer: 1')
		elif data == 1:
			print('Answer: 1')
		elif data > 1:
			fact = 1
			while data > 1:
				fact *= data
				data -= 1
			print('Answer: ' + str(fact))
		while True:
			data = int(input('Give me a number, and I will list the answer of factorial: '))
			if data == EXIT:
				print('------ See ya! ------')
				break
			elif data == 0:
				print('Answer: 1')
			elif data == 1:
				print('Answer: 1')
			elif data > 1:
				fact = 1
				while data > 1:
					fact = fact * data
					data -= 1
				print('Answer: ' + str(fact))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()