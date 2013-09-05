'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

'''
If a is odd, then b = a2/2 ? 1/2 and c = b + 1
If a is even, then b = a2/4 ? 1 and c = b + 2

a=2n+1
b=2n(n+1)
c=2n(n+1)+1
'''
import time
def triple():
	start = time.time()
	for a in range (1,1000):
		for b in range(1,1000):
			for c in range(1,1000):
				if a+b+c ==1000:
					if (a**2) + (b**2) == (c**2):
						return "%s found in %s seconds" % (a*b*c,time.time() -start)

print triple()


















#def triplet(a,n):
#	#a = (2.0*n) +1.0
#	b = (2.0*n)*(n+1.0)
#	c = (2.0*n)*(n+1.0) +1.0
#	
#	'''
#	if 1000 % (a+b+c) ==0
#	'''
#	
#	if a+b+c == 1000:
#		return a*b*c
#	elif a+b+c > 1000:
#		return 'no triplet found -> ' + str(a+b+c) + " -> " + str(n)
#	else:
#		print "a = " + str(a) + " b = " + str(b) + " c = " + str(c) + " -> " + str(a+b+c)+ " -> " + str(n)
#		return triplet(a+1,((a+1)-1)/2)
#
#n = 1
#a = 1
#n=(a-1)/2
#print triplet(a,n)