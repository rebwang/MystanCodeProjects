"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
lar = 0


def main():
	global lar
	print(find_largest_digit(12345))      # 5
	lar = 0  # reset lar before executing next function
	print(find_largest_digit(281))        # 8
	lar = 0
	print(find_largest_digit(6))          # 6
	lar = 0
	print(find_largest_digit(-111))       # 1
	lar = 0
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: an integer made of digits, the integer can be negative
	:return: the largest digit in the n integer
	"""
	global lar
	num = abs(n)
	if num != 0:
		r = num % 10
		if r > lar:
			lar = r
		find_largest_digit(int(num/10))
	return lar








if __name__ == '__main__':
	main()
