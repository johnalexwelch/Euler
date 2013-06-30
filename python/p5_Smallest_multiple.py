'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def multiple(x):
	check = True

	for i in range(1,20):

		if x%i != 0:
			check = False
			break
	return check

def count_function(n):
	
	check = multiple(n)
	while check != True:
		n+=20
		check = multiple(n)

	print n
	

print count_function(20)