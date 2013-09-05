'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import time

def multiple(x):
	check = True

	for i in range(1,20):

		if x%i != 0:
			check = False
			break
	return check

def count_function(n):
	start = time.time()	
	check = multiple(n)
	while check != True:
		n+=20
		check = multiple(n)

	return "%s found in %s seconds" % (n,time.time() - start)

print count_function(20)