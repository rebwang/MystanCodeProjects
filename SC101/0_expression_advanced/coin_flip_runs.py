"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Flip a coin for n times until the number of runs reach user's input.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	run = 0
	ans = ""
	roll1 = r.randint(1, 2)
	ans += str(roll1)
	is_in_a_row = False  # A on/off switch to control when to calculate a run
	while True:  # Flip coin n times
		if run == num_run:
			break
		roll2 = r.randint(1, 2)
		ans += str(roll2)
		if roll1 == roll2:
			if not is_in_a_row:
				run += 1
				is_in_a_row = True  # Turn on the switch when there is consecutive result
		else:
			is_in_a_row = False  # Reset the switch when the consecutive result stops
		roll1 = roll2

	# replace numbers with characters H & T
	new_ans = ""
	for ch in ans:
		if ch == '1':
			new_ans += 'H'
		else:
			new_ans += 'T'
	print(new_ans)




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
