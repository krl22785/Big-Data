#!/usr/bin/python

import sys
import os

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")
	
	medallion = eval(splits[0])[0]
	print "%s\t%s" % (medallion, 1) 	


 


	
