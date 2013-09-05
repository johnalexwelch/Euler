'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Numbers in file p13.txt
'''
import time
def addition(f):
	total = 0
	for i in f:
		total += int(i)
	
	elapsed = time.time() - start
	return "%s found in %s seconds" % (str(total)[:10],elapsed)

start = time.time()
with open('txt_files/p13.txt','rU') as f:
	content = f.readlines()
	
print addition(content)