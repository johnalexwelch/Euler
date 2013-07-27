'''A 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
What is the total of all the name scores in the file?
'''

alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}

f = open('txt_files/names.txt','rU')

line = f.readlines()
f.close()
i=line[0]
name_in = i.split(',')
names = [', '.join(name_in[n:]) for n in range(len(name_in))]
print names
#names = line.split(",")
