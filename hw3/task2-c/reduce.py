#!/usr/bin/env python

import sys

current_key = None 
current_fares = [0]
current_trips = [0] 
finalAttributes = []
passenger_distribution = {}  
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
		
		passenger_amount = allAttributes[10] 		 		
		

		if passenger_amount in passenger_distribution:
			passenger_distribution[passenger_amount] += 1
		else:
			passenger_distribution[passenger_amount] = 1 

finalOutput = sorted(passenger_distribution.items(), key = lambda x: -x[1]) 

for pas in finalOutput:
	print "%s\t%s" % (pas[0], pas[1])  
		
#if current_key == key:
#	allAttributes =  []
 #       allAttributes.extend(current_fares)
  #      allAttributes.extend(current_trips)
