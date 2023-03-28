question = 1

# ------ Question 1 -------
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

if question == 1:
	print(*(i for i in range(2000, 3201) if (i % 7 == 0) and (i % 5 != 0)), sep=',')

# ------ Question 2 -------
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

if question == 2:
	while True:
		try:
			number = int(input('Type a number equal or higher than 0:'))
			if number < 0:
				raise ValueError
		except ValueError or TypeError:
			print('Wrong input! Try again.')
		else:
			break

	factorial = 1

	for i in range(1, number+1):
		factorial *= i

	print(f'Factorial of that number is {factorial}')

# ------ Question 2 -------
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
#
# Then, the output should be:
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

if question == 3:
	while True:
		try:
			number = int(input('Type a number higher than 0:'))
			if number < 1:
				raise ValueError
		except ValueError:
			print("Wrong input! Try again.")
		else:
			break

	print({i: i*i for i in range(1, number+1)})
