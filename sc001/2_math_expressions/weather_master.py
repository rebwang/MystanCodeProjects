"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	The weather master will show 4 elements in the end: average, highest, lowest, cold days
	Highest temperature & lowest temperature: compare every new given data with the old max & old min
	Average temperature: need to know the sum and count for all given temperatures. The result will be sum divided by count
	Cold days: create a variable for cold days, compare every new given data with 16, and count by adding 1 to the variable
	"""
	print('stanCode "Weather Master 4.0"!')
	data = int(input('Next Temperature: (or -100 to quit)? '))
	cold_day = 0
	temp_sum = 0
	count_data = 0
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		count_data += 1
		temp_sum += data
		maximum = data
		minimum = data
		if data < 16:
			cold_day += 1
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data == EXIT:
				break
			if data < 16:
				cold_day += 1
			if data > maximum:
				maximum = data
			elif data < minimum:
				minimum = data
			count_data += 1
			temp_sum += data
		avg_temp = temp_sum / count_data
		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = '+str(avg_temp))
		print(str(cold_day)+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
