#!/usr/bin/python

import sys
import os
import csv

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")

	values = eval(splits[1]) 

	type = values[24]
	total = values[18]
	tip = values[16] 

	value_outputs = (1, total, tip)

	print "%s\t%s" % (type, value_outputs) 

