'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import time
def sum_of_digits(x):
	start = time.time()
	digitlist = str(2**x)
	total = 0
	for i in digitlist:
		total += int(i)
	elapsed = time.time() - start
	return "%s found in %s seconds" % (total,elapsed)

print sum_of_digits(1000)