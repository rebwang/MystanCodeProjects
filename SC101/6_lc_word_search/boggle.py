"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Input a 4*4 word board. Constraints:
	1. case-insensitive
	2. Input format: must have space in between of characters
	"""
	start = time.time()

	board = []
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if len(row) != 7:
			print('Illegal input')
			break
		else:
			lst = []
			for ch in row:
				if ch != ' ':
					lst.append(ch.lower())  # case-insensitive
			board.append(lst)
	find_word(board)

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(board):
	dic = read_dictionary()
	word_lst = []

	def find_word_helper(board, dic, word_lst, current_s, x, y, passed):
		# base case
		if len(current_s) >= 4:
			if current_s in dic and current_s not in word_lst:
				word_lst.append(current_s)
				print(f'Found "{current_s}"')

		if has_prefix(current_s, dic):
			for i in range(-1, 2):
				for j in range(-1, 2):
					new_x = x + i
					new_y = y + j
					if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_x, new_y) not in passed:  # make sure x,y not exceed 4x4 board
						current_s += board[new_x][new_y]
						passed.append((new_x, new_y))
						find_word_helper(board, dic, word_lst, current_s, new_x, new_y, passed)
						current_s = current_s[:-1]
						passed.pop()

	for i in range(0, 4):
		for j in range(0, 4):
			passed = []
			find_word_helper(board, dic, word_lst, "", i, j, passed)

	print(f'There are {len(word_lst)} words in total.')


# def find_word_helper(board, dic, word_lst, counter, current_s, x, y, passed):
# 	# base case
# 	if len(current_s) >= 4:
# 		if current_s in dic and current_s not in word_lst:
# 			word_lst.append(current_s)
# 			counter += 1
# 			print(f'Found "{current_s}"')
#
# 	if has_prefix(current_s, dic):
# 		# choose
# 		for i in range(-1, 2):
# 			for j in range(-1, 2):
# 				new_x = x+i
# 				new_y = y+j
# 				if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_x, new_y) not in passed:
# 					current_s += board[new_x][new_y]
# 					passed.append((new_x, new_y))
# 					find_word_helper(board, dic, word_lst, counter, current_s, new_x, new_y, passed)
# 					current_s = current_s[:-1]
# 					passed.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >=4:
				dic += word.split()
	return dic


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
