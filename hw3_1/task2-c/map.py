#!/usr/bin/python

import sys
import os

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")
	
	passengers = eval(splits[1])[3] 
	print "%s\t%s" % (passengers, 1) 


	
