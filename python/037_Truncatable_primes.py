'''
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import time

def truncate_right(n):
	num =  str(n)[:1]
	if prime(num) == True:
		if len(num) == 1:		
			return True
		else:
			return truncate_right(num)
	else:
		return False

def truncate_left(n):
	num =  str(n)[1:]
	if prime(num) == True:
		if len(num) == 1:		
			return True
		else:
			return truncate_left(num)
	else:
		return False
	
	
def prime(n):
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

def main():
	count = 0
	total = 0
	p = 113
	
	while count < 11:
		if prime(p) == True:
			if truncate_left(p) == True:
				if truncate_right(p) == True:
					count += 1
					total += p
					print total
		p+=1
		
		
	return "%s found in %s seconds" % (total,time.time() - start)
if __name__ == '__main__':
	start = time.time()
	main()