'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math

def prime(fl):
	for j in fl:
		if ((j%2 ==0) and (j/2 != 1)):
			break
		elif (j%3 ==0) and (j/3 != 1):
			break
		elif (j%5 ==0) and (j/5 != 1):
			break
		elif (j%7 ==0) and (j/7 != 1):
			break
		elif (j%11 ==0) and (j/11 != 1):
			break
		elif (j%13 ==0) and (j/13 != 1):
			break
		else:
			print str(j) + ' is a possible prime'
		
def factors(n):
	factor_list =[]
	for i in xrange(2,n):
		if n%i == 0:
			factor_list.append(i)
	print factor_list
	return prime(factor_list)
			
			
print factors(600851475143)