#!/usr/bin/env python

import sys

current_key = None 
current_fares = [0]
current_trips = [0] 
finalAttributes = []
medallion_trips = {} 


for line in sys.stdin:
	
	key, value = line.split('\t')				 
	value = eval(value)

	tableName = value[0]

	tempAttributes = value[1]
	tableAttributes = tempAttributes.split(",") 
	 
	if key != current_key: 
		current_key = key 
		
		if tableName == 'fares':
			current_fares = tableAttributes
		else:
			current_trips = tableAttributes  
	else:
		if tableName == 'trips':
			current_trips = tableAttributes
		else:
			current_fares = tableAttributes  
		
		allAttributes = [] 
		allAttributes.extend(current_fares)
		allAttributes.extend(current_trips)
		
		temp = eval(key)
		medallion = temp[0]

		if medallion not in medallion_trips:
			medallion_trips[medallion] = 1
		else:
			medallion_trips[medallion] += 1  		 		
		
finalOutput = sorted(medallion_trips.items(), key = lambda x: -x[1]) 

for med in finalOutput:

	print "%s\t%s" % (med[0], med[1]) 

