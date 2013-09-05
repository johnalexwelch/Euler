'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time
def palindrome(n):
	p = str(n)[::-1]
	
	if n == int(p) :
		return True
	else:
		return False

def product():
	start = time.time()
	h = 0
	for i in range(100,999):
		for j in range(100,999):
			n = i*j
			if palindrome(n) == True:
				if n > h:
					h = n
	
	return "%s found in %s seconds" % (h,time.time() - start)			

print product()
