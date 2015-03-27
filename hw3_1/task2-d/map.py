#!/usr/bin/python

import sys
import os

for line in sys.stdin:

	line = line.strip()
	splits = line.split("\t")
	
	pickup = eval(splits[0])[3][0:10] 	
	fare = eval(splits[1])[11]
	surcharge = eval(splits[1])[12]
	tips = eval(splits[1])[14]
	tolls = eval(splits[1])[15]
	
	all_values = (fare, surcharge, tips, tolls) 
	
	print "%s\t%s" % (pickup, all_values) 

	
