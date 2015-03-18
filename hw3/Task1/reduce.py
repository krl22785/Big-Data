#!/usr/bin/env python

import sys


current_key = None 
current_fares = [0]
current_trips = [0] 
finalAttributes = [] 

for line in sys.stdin:
	
	key, value = line.split('\t')				 
	value = eval(value)

	tableName = value[0]

	tempAttributes = value[1]
	tableAttributes = tempAttributes.split(",") 
	
	if key == current_key:

		if tableName == 'fares':
                        current_fares = tableAttributes
                else:
                        current_trips = tableAttributes
	else:
		
		if current_key:  
			#print "%s\t%s" % (current_key, finalAttributes) 
			allAttributes =  [] 
			allAttributes.extend(current_fares)
			allAttributes.extend(current_trips)  
			
			print "%s\t%s" % (key, allAttributes) 
	
		current_key = key 
		if tableName == 'fares':
                        current_fares = tableAttributes
                else:
                        current_trips = tableAttributes
		
		
if current_key == key:
	allAttributes =  []
        allAttributes.extend(current_fares)
        allAttributes.extend(current_trips)
