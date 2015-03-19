#!/usr/bin/env python

import sys

current_key = None 
current_fares = [0]
current_trips = [0] 
finalAttributes = []
fare_distribution = {}  
above10 = 0 


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
		
		fare_amount = allAttributes[1] 		
		fare_amount = float(fare_amount) 		
		

		if fare_amount <= 10.00:
			above10 +=1 
		else:
			pass

print above10 
		
#if current_key == key:
#	allAttributes =  []
 #       allAttributes.extend(current_fares)
  #      allAttributes.extend(current_trips)
