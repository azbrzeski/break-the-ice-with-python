from functools import reduce

question = 13


# --------- Question 10 ------------
# Write a program that accepts a sequence of whitespace separated words as input and prints
# the words after removing all duplicate words and sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
# Then, the output should be:
#
# again and hello makes perfect practice world

if question == 10:

	sequence = sorted(list(set(input('Type in white space separated word sequence:').split())))

	print(' '.join(sequence))


# --------- Question 11 ------------
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
# whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
# Example:
#
# 0100,0011,1010,1001
# Then the output should be:
#
# 1010
# Notes: Assume the data is input by console.

if question == 11:
	seq = input('Type in a sequence of 4-digit binary numbers:').split(',')

	div_5 = []
	for i in range(len(seq)):
		if (int(seq[i], base=2)) % 5 == 0:
			div_5.append(seq[i])

	print(','.join(div_5))


# --------- Question 12 ------------
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

if question == 12:

	def even_div10(num):
		temp = num
		while temp > 0:
			if temp % 2 != 0:
				return None
			temp = temp//10

		return num

	seq = []
	for i in range(1000, 3001):
		a = even_div10(i)
		if a:
			seq.append(a)

	print(','.join(map(str, seq)))


	def reduce_even(bool_var, num):
		return int(num) % 2 == 0 and bool_var

	seq1 = [i for i in range(1000, 3001) if reduce(reduce_even, str(i), True)]

	print(','.join(map(str, seq1)))


# --------- Question 13 ------------
# Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3

if question == 13:

	seq = input('Type text:')
	letters = 0
	numbers = 0

	for i in seq:
		if i.isalpha():
			letters += 1
		elif i.isdigit():
			numbers += 1

	print(f'LETTERS: {letters}\nNUMBERS: {numbers}')
