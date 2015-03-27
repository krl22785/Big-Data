#!/usr/bin/python

import sys
import os

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")
	
	total = eval(splits[1])[16]
	total = float(total)

	if total <= 10.00:
		print "%s\t%s" % (total, 1) 
	else:
		pass 

	
