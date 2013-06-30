'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def isprime(n):
    n = abs(int(n))

    if n < 2:
        return False

    if n == 2: 
        return True    

    if not n & 1: 
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def loop_prime(n):
	counter = 0
	l_prime = 1
	while counter < 10001:
		check = isprime(n)
		if check != True:
			n+=1
		else:
			counter +=1
			l_prime = n
			n+=1
	return l_prime	
print loop_prime(1)
