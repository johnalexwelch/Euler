'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
'''
import time
def binomial(n,k):
	total = 1
	
	if k > n-k:
		k = n-k
		
	for i in range(1,k+1):
		total *= (n - (k - i))
		total /= i
	
	return "%s found in %s seconds" % (total,time.time() - start)

start = time.time()
sides = 20
n = sides *2
k = sides
if __name__=='__main__':
	print binomial(n,k)