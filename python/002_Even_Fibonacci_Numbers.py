'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
import time
def fib():
	start = time.time()
	a,b = 0,1
	total =0
	for i in range(1,100000):
		if a > 4000000:
			elapsed = time.time() - start
			return "%s found in %s seconds" % (total,time.time() - start)
		elif a%2 != 0:
			
			a, b = b, a+b
		else:
			total+=a
			a, b = b, a+b
	
	
print fib()