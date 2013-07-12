'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def sum_of_digits(x):
	digitlist = str(2**x)
	total = 0
	for i in digitlist:
		total += int(i)
	return total

print sum_of_digits(1000)