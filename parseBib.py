import re
import fileinput
import sys
import csv

# inilialize variable
# Title = ""
# DOI = ""
title_id = {}
ID=""
Title = ""
# Volumn = ""
# Issue = ""
# Start_page = ""
# End_page = ""
# N_of_page = ""
# N_of_author = ""
# N_of_keyword = ""
# Abstract = ""

# f = open('output2.csv', 'a')
# writer = csv.writer(f)
# writer.writerow( ('Title', 'DOI', 'ISSN', 'Volumn', 'Issue', 'N_of_page', 'N_of_author', 'N_of_keyword') )
# fout = open(sys.stdout, 'a')
fin = open('test_bib','r')

for line in fin:    
	
	if line.startswith('@'):
		# print line
		elements = re.split('@|{|, \n|\t|\r', line)
		print elements[1] + '\t' + elements[2]
		ID = elements[2]
	elif line.startswith('title'):
		# print line
		elements = re.split('={|},', line)
		print elements[0] + '\t' + elements[1]
		Title = elements[1]
		title_id[Title] = ID
		ID=""
		Title = ""

temp = 'Raytracing Dynamic Scenes on the GPU Using Grids'
print title_id	
print title_id[temp]
		    


fin.close()
# f.close()

