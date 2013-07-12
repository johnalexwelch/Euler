'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
	
def is_odd(n):
	return (3*n)+1

def is_even(n):
	return n/2

def ooe(n):
	# Determins if the number is odd or even
	if n%2 == 0 :
		return True
	else:
		return False

def collatz(n, c_list):
	c_list.append(n)
	if n == 1:
		return c_list
	else:
		if ooe(n) == True:
			return collatz(is_even(n), c_list)
		else:
			return collatz(is_odd(n), c_list)

def main():
	total = 0
	for i in range(13,1000000):
		count = len(collatz(i,[]))
		if count > total:
			total = count
			n = i
	return n

print main()