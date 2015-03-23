#!/usr/bin/env python

import sys
import csv
import StringIO
n = 0

for line in sys.stdin:	
	key, value = line.split('\t')
	
	value1 = eval(value)
	
	print value1[0]
	
	#value1 = eval(value)
	#print value1[1].split("??")[0]

	#csv_file = StringIO.StringIO(line)
   	#csv_reader = csv.reader(csv_file)
    	
	#for record in csv_reader:
	#	print record
