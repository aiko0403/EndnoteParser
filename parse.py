import re
import fileinput
import sys

r = re.compile(' - ')
i=0
j=0

for line in fileinput.input():    
	i=i+1
	print i
	j=0
	elements = r.split(line)
	#elements = line.replace('-',' ').split()
	# elements = r.split(line)

	# for value in elements:
	# 	j=j+1
	# 	value = value.rstrip()
	# 	value = value.split('\r\t\n')
	# 	print("|" + str(j) + value[0]  + "|")
	if i==2:
		continue
	elements[0] = elements[0].rstrip().split('\r\t\n')
	elements[1] = elements[1].rstrip().split('\r\t\n')

	if elements[0]=='TI':
		print('Title '+elements[1])
	else if elements[0]=='DO':
		print('DOI '+element)
		pass


fileinput.close()





# f = open('filename')
# lines = f.readlines()


# r.split("abc:def  ghi")


# f.close()