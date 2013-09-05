total = 0

for i in range(2,1000000):
	check = 0
	for j in str(i):
		check += int(j)**5
	
	if check == i:
		total += check
		
print total

	
