import re
import fileinput
import sys

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


# fout = open(sys.stdout, 'a')

for line in fileinput.input():    
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
		N_of_page = ""
		N_of_author = ""
		N_of_keyword = ""
		Abstract = ""
	
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
	elif ''.join( elements[0] ) == 'DO':
		print 'DOI ' + ''.join( elements[1] )
		DOI = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'SN':
		print 'ISSN ' + ''.join( elements[1] )
		ISSN = ''.join( elements[1] )
	elif ''.join( elements[0] ) == 'VO':
		print 'Volumn ' + ''.join( elements[1] )
		Volumn = ''.join( elements[1] )


fileinput.close()



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