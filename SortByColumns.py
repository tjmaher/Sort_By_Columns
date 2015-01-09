#   Thomas F. Maher, Jr. ('T.J.')
#   tj.maher@gmail.com 
#  	Senior QA Lead / BSCS / Masters of Software Engineering
#  	Write a program that takes as its first argument the name of an input file 
#  (such as the attached testfile.txt), a second argument is a primary column to sort
# 	by in ascending order, and a third argument as a secondary column to sort by 
#	(also in ascending order).  Null values or empty strings should always be last 
#	in the sort order. 
#  	
#	So if Python 2.7 is installed on the computer, and if in the directory where 
# 	the files 'SortByColumns.py' and 'textfile.txt' you input on the command line:
#   
# 	> python SortByColumns.py testfile.txt Gender Name 
#
# 	The output would be:
#
#  	ID		Name	Gender	Age
#  	EMP5	Dana	F	
#  	EMP2	Sally	F	30

from sys import argv
import operator
import csv
from collections import defaultdict

# Get the arguments from the command line such as:
# > python SortByColumns.py testfile.txt Gender Name
scriptName, inputFile, sortPrimary, sortSecondary = argv

print "*" * 10
print "SortByColumns.py"
print "*" * 10

print "\nThe Python 2.7 program %s will:" % scriptName
print "* Read the arguments listed when this program was started such as."
print "\t > python SortByColumns.py testfile.txt Gender Name"
print "* Open the tab separated input file: %s" % inputFile
print "* Read the column heading into a Dictionary as the keys, \n\t with data below headings as the values"
print "* Print out a list sorted by %s and %s." % (sortPrimary, sortSecondary)


# The CSV Module normally reads Comma Separated Value files: (ID, Name, Gender..)
# But for our input file, we have different columns to be separated by Tabs. ('\t').
# Open INPUTFILE, which in this case is 'textfile.txt', to be read-only ('r').
# The CSV Module will use the Dictionary Reader method to take that first column
# and store what it finds -- i.e. ID, Name, Gender, and Age -- as keys, and 
# everything below the column headers will be values indexed by the keys.

with open(inputFile, 'r') as f:
	print "\n... Reading file: %s..." % inputFile
	reader = csv.DictReader(f, delimiter='\t')
	print "... Reading data into the dictionary using DictReader..." 

# for row in reader: # Iterates through all rows in Dictionary we have captured in READER
# 	print row
# ==> 'Gender': 'M', 'Age': '23', 'ID': 'EMP1', 'Name' : 'Jim' (... etc) 

	print "... Sorting data by primary and secondary keys: %s, %s ..." % (sortPrimary, sortSecondary)
	data = sorted(reader, key=operator.itemgetter(sortPrimary, sortSecondary))
	
	outputFileName = 'sorted_' + inputFile

	print "... Creating a new output file: %s..."  % outputFileName
	outputFile = open(outputFileName, 'w')
	
	print "... Setting the headers of the input file as the output file..."
	fieldnames = reader.fieldnames

	print "... Setting up output file as a tab delineated text file..."
	writer = csv.DictWriter(outputFile, fieldnames, delimiter = '\t')
	
	print "... Writing the column headings ..."
	writer.writeheader()
	
	print "... Writing the column values ..."
	writer.writerows(data)
	
	print "\n... DONE! ... "
	print "\nPlease locate the output file %s in the current directory to view the sorted data.\n" % outputFileName  