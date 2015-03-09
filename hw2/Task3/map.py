#!/usr/bin/python

import sys
import csv
import string 

f = open("stop-word-list.csv")
reader = csv.reader(f) 
stop = reader.next()
stopList = []

for word in stop:
	stopList.append(word.strip()) 

punc = string.punctuation
digi = string.digits 

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	l = line.strip().split()
    
   	for word in l:	
	
		updatedWord = word.translate(None, punc + digi).lower()
       
		if len(updatedWord) != 7:
			pass
		else:
			if updatedWord not in stopList: 
       				print "%s\t%d" %(updatedWord, 1)  
	
        	

