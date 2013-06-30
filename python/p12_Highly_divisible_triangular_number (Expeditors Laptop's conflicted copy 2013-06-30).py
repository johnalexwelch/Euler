'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
def natural_nums(l):
	numlist = []
	total = 0
	numlist = l
	
	for i in numlist:
		total +=i
	
	if divisor(total) == 5:
		True
	else:
		print total
		print numlist
		newlist = numlist.append(total)
		print newlist
		#return natural_nums(numlist.append(total))

def divisor(x):
	div_count = 0
	for i in xrange(1, (x/2) + 1):
		if x%i == 0 :
			div_count +=1
	return x
	

nList = [1,2,3,4,5,6,7]
print natural_nums(nList)
#print divisor(2800000000)