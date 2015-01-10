# Sort_By_Columns
Python 2.7: " a program that takes as its first argument the name of an input file 
(such as included "testfile.txt"), a second argument is a primary column to sort
by in ascending order, and a third argument as a secondary column to sort by 
(also in ascending order)". 

So if Python 2.7 is installed on the computer, and if in the directory where 
the files 'SortByColumns.py' and 'textfile.txt' you input on the command line:
   
 	> python SortByColumns.py testfile.txt Gender Name 

 	The output file would be:

  	ID		Name	Gender	Age
  	EMP5	Dana	F	
  	EMP2	Sally	F	30
  	
Demonstrates:
* How to read files into a Dictionary with DictReader from a tab delimited file
* How to sort the Dictionary
* How to output a dictionary to a table in an output file using DictWriter
