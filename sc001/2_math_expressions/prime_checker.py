"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	The prime checker will divide the given number by 2,3 and 5 to determine if the remainder is 0.
	If any above scenario makes the remainder 0, then the given number is not a prime number, other than that,
	the given number is a prime number.
	"""
	print('Welcome to the prime checker!')
	data = int(input('n: '))
	if data == EXIT:
		print('Have a good one!')
	else:
		# First step: determine the given number is odd or even, because most prime numbers are odd except 2.
		if data % 2 == 0:
			if data == 2:
				print(str(data) + ' is a prime number')
			else:
				print(str(data) + ' is not a prime number')
		else:
			if data == 3:
				print(str(data) + ' is a prime number')
			if data == 5:
				print(str(data) + ' is a prime number')
			if data % 3 != 0:
				if data % 5 != 0:
					print(str(data) + ' is a prime number')
			else:
				if data != 3:
					print(str(data) + ' is not a prime number')
		while True:
			data = int(input('n: '))
			if data == EXIT:
				print('Have a good one!')
				break
			if data % 2 == 0:
				if data == 2:
					print(str(data) + ' is a prime number')
				else:
					print(str(data) + ' is not a prime number')
			else:
				if data == 3:
					print(str(data) + ' is a prime number')
				if data == 5:
					print(str(data) + ' is a prime number')
				if data % 3 != 0:
					if data % 5 != 0:
						print(str(data) + ' is a prime number')
				else:
					if data != 3:
						print(str(data) + ' is not a prime number')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
