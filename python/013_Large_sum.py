'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Numbers in file p13.txt
'''
def addition(f):
	total = 0
	for i in f:
		total += int(i)
	return str(total)[:10]

with open('p13.txt','rU') as f:
	content = f.readlines()
	
print addition(content)