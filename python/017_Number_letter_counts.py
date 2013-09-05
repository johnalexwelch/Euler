'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''
import time

single = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
double = [0,3,6,6,5,5,5,7,6,6]

def to_words(n):
	start = time.time()
	total = 0
	
	for i in xrange(1,n+1):
		if i < 20:
			total += single[i]
		elif i < 100:
			total += double[i/10] + single[i%10]
		elif i < 1000:

			#Add 7 for the "hundred"
			total += single[i/100] +  7
			
			if ((i/10)%10) < 2:
				total += single[i%100]
			else:
				total += double[(i/10)%10] + single[(i%10)%10]
			
			# Handle the "and"
			if (((i/10)%10 != 0) or ((i%10)%10 != 0)):
				total += 3
		
		else: total += single[1] + 8 #Add 8 for the thousand
	elapsed = time.time() - start
	return "%s found in %s seconds" % (total,elapsed)

#21124
print to_words(1000)

## TESTING AREA ##
#def test(i):
#	total = 0
#	print "Digit Value"
#	print str((i/100)) + "         ->  " + str(single[i/100])
#	print str((i/10)%10)  + "         ->  " + str(double[(i/10)%10])
#	print  str((i%10)%10) + "         ->  " + str(single[(i%10)%10])
#	
#	if i < 20:
#		total += single[i]
#	elif i < 100:
#		total += double[i/10] + single[i%10]
#	elif i < 1000:
#
#	#Add 7 for the "hundred"
#		total += single[i/100] +  7
#		print  "hundred   ->  7"
#			
#		if (i/10) < 0:
#			total += single[1/10]
#		else:
#			if ((i/10)%10) < 2:
#				#print i%100
#				total += single[i%100]
#			else:
#				total += double[(i/10)%10] + single[(i%10)%10]
#			
#			#print double[(i/10/10)]
#		# Handle the "and"
#		if (((i/10)%10 != 0) or ((i%10)%10 != 0)):
#			print  "and       ->  3"
#			total += 3
#		
#	else: total += single[1] + 8 #Add 8 for the thousand
#	
#	print "------------------"
#	return total
#print test(817)