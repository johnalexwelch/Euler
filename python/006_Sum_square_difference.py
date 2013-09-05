'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import time
def sum_of_square():
	ss = 0
	
	for i in range(1,101):
		ss+=(i**2)
	
	return ss

def square_of_sum():
	ss = 0
	for i in range(1,101):
		ss+=i
		ss2 = ss**2
	
	return ss2
	
def diff():
	start = time.time()
	
	diff = square_of_sum() - sum_of_square()
	
	return "%s found in %s seconds" % (diff,time.time() - start)

#print sum_of_square()
#print square_of_sum()
print diff()
