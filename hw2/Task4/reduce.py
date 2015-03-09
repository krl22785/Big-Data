#!/usr/bin/python

import sys
import csv

current_word = None
current_doc = None
current_sum = 0
master_dict = {}


def outputwords(items, current_word):
	n = 0 
	items.insert(0, current_word)
	cnt = len(items)

	for i, line in enumerate(items):
		if i == 0:
			print line,"\t",
		elif i == cnt - 1:
			print "%s %s" % (line[0], line[1]),
		else:
			print "%s %s, " % (line[0], line[1]),
	print			


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    word, doc, count = line.strip().split()
    doc = doc[2:-2]
    count = count[:-1]

   # print word, doc, count

    try:
        count = int(count)
    except ValueError:
        continue

    if word == current_word:
        if doc == current_doc:
                master_dict[current_word][doc] += count 
        else:
                master_dict[current_word][doc] = current_sum 
    else:
        if current_word:
	
		final = sorted(master_dict[current_word].items(), key = lambda x:(-x[1], x[0]))
		outputwords(final, current_word) 

		##########print current_word, final, len(final   
		#####for i in 
		#####	print "%s\t%s %s,\n" % (current_word, i[0], i[1]),  
		

        current_word = word
        current_sum = count
        current_doc = doc
	master_dict[current_word] = {}
	master_dict[current_word][current_doc] = current_sum  

if current_word == word:
	final = sorted(master_dict[current_word].items(), key = lambda x:(-x[1], x[0]))
	outputwords(final, current_word)
#    master_dict[current_word][current_doc] = current_sum


