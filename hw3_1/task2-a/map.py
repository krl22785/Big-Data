#!/usr/bin/python

import sys
import os

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")
	
	fare = eval(splits[1])[11]
	print "%s\t%s" % (fare, 1) 

	
