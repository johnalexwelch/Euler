
p_list = [1,2,3,10,20,50,100,200]

def two_pounds():
	count = 0
	for a in range(0,201):	#1 p
		print 1
		for b in range(0,101):  #2 p
			total = a*1 + b*2
			if total == 200:
				print total
				count += 1
				break
			if total > 200:
				break
			
			for c in range(0,34):	#3 p
				total = a*1 + b*2 + c*3 
				if total == 200:
					print total
					count += 1
					break
				if total > 200:
					break
				
				for d in range(0,21):	#10 p
					total = a*1 + b*2 + c*3 + d*10 
					if total == 200:
						print total
						count += 1
						break
					if total > 200:
						break
					
					for e in range(0,11):	#20p
						total = a*1 + b*2 + c*3 + d*10 + e*20 
						if total== 200:
							print total
							count += 1
							break
						if total > 200:
							break
						
						for f in range(0,5):	#50 p
							total = a*1 + b*2 + c*3 + d*10 + e*20 + f*50
							if total== 200:
								print total
								count += 1
								break
							if total > 200:
								break
							
							for g in range(0,3):	#1 pound
								total = a*1 + b*2 + c*3 + d*10 + e*20 + f*50 + g*100
								if total == 200:
									print total
									count += 1
									break
								if total > 200:
									break
								for h in range(1,2):	#2 pounds
									if a*1 + b*2 + c*3 + d*10 + e*20 + f*50 + g*100 + h*200 == 200:
										print 200
										count += 1
	return count
									
print two_pounds()
#a*1 + b*2 + c*3 + d*10 + e*20 + f*50 + g*100 + h*200