#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []

for line in sys.stdin:
        
	key, value = line.split('\t')
	value = eval(value) 

	tableName = value[0]
	tempAttributes = value[1]
	tableAttributes = tempAttributes.split(",")        

	if key.count(",") == 3:
		medallion_key = eval(key)[0] 
	else:
		compare_key = key 


	
