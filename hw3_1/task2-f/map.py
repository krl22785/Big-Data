#!/usr/bin/python

import sys
import os

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")
	
	hack_license = eval(splits[0])[1]
	medallion = eval(splits[0])[0]

	print "%s\t%s" % (hack_license, medallion) 	


 


	
