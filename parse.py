import re
import fileinput
import sys
import csv

fin = open('BibTex/201201.rtf','r')
fin2 = open('EndNote/201201','r')
fout = open('output_all.csv', 'a')

title_id = {}
bib_ID=""
bib_Title = ""

for line in fin:    
	
	if line.startswith('@'):
		# print line
		elements = re.split('@|{|, \n|\t|\r', line)
		print elements[1] + '\t' + elements[2]
		bib_ID = elements[2]
	elif line.startswith('title'):
		# print line
		elements = re.split('={|},', line)
		print elements[0] + '\t' + elements[1]
		bib_Title = elements[1]
		title_id[bib_Title] = bib_ID
		bib_ID=""
		bib_Title = ""

# print title_id	
		    
fin.close()

r = re.compile(' - ')

# inilialize variable
Title = ""
DOI = ""
ISSN = ""
Volumn = ""
Issue = ""
Start_page = ""
End_page = ""
N_of_page = ""
N_of_author = ""
N_of_keyword = ""
Abstract = ""
ID = ""


writer = csv.writer(fout)
writer.writerow( ('ID','Title', 'DOI', 'ISSN', 'Volumn', 'Issue', 'N_of_page', 'N_of_author', 'N_of_keyword') )
# fout = open(sys.stdout, 'a')

for line in fin2: #fileinput.input():    
	elements = r.split(line)

	if len(elements) <2:
		continue
	
	elements[0] = elements[0].rstrip().split('\r\t\n')
	elements[1] = elements[1].rstrip().split('\r\t\n')

	if ''.join(elements[0])=='TY':
		# inilialize variable
		Title = ""
		DOI = ""
		ISSN = ""
		Volumn = ""
		Issue = ""
		Start_page = ""
		End_page = ""
		N_of_page = 0
		N_of_author = 0
		N_of_keyword = 0
		Abstract = ""
		ID = ""
	
	if ''.join( elements[0] ) == 'TI':
		print 'Title ' + ''.join( elements[1] )
		Title = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'DO':
		print 'DOI ' + ''.join( elements[1] )
		DOI = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'SN':
		print 'ISSN ' + ''.join( elements[1] )
		ISSN = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'VO':
		print 'Volumn ' + ''.join( elements[1] )
		Volumn = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'IS':
		print 'Issue ' + ''.join( elements[1] )
		Issue = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'SP':
		print 'Start_page ' + ''.join( elements[1] )
		Start_page = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'EP':
		print 'End_page ' + ''.join( elements[1] )
		End_page = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'AB':
		print 'Abstract ' + ''.join( elements[1] )
		Abstract = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'AU':
		# print 'ISSN ' + ''.join( elements[1] )
		N_of_author += 1
	elif ''.join( elements[0] ) == 'KW':
		# print 'Volumn ' + ''.join( elements[1] )
		N_of_keyword += 1
	elif ''.join( elements[0] ) == 'ER':
		N_of_page = int(End_page) - int(Start_page) + 1
		ID = title_id[Title]

		print 'N_of_page ' + str( N_of_page )
		print 'N_of_author ' + str( N_of_author )
		print 'N_of_keyword ' + str( N_of_keyword )

		

		# print out json here  
		    
		writer.writerow( (ID, Title, DOI, ISSN, Volumn, Issue, N_of_page, N_of_author, N_of_keyword) )

		
		    


fin2.close()
fout.close()


# ISSN
# Volumn
# Issue
# Start page
# End page
# # of page (calculate)
# Author array
# # of author (calculate)
# Keyword array
# # of keyword (calculate)
# Abstract



# f = open('filename')
# lines = f.readlines()


# r.split("abc:def  ghi")


# f.close()