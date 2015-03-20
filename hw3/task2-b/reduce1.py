#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
above10 = 0 

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
 			 
               	allAttributes = []
                allAttributes.extend(current_trips)
                allAttributes.extend(current_fares)
		
		if len(allAttributes) == 17:  #make sure each key appears in both 
		
                	fare_amount = allAttributes[11]
			fare_amount = float(fare_amount) 

			if fare_amount <= 10.00:
				above10 += 1
			else:
				pass

			current_trips = [] 
			current_fares = [] 	
			current_key = key
	
			if tableName == 'fares':
        	               	current_fares = tableAttributes
               		else:
                       		current_trips = tableAttributes
		else: 
			current_trips = []
                        current_fares = []
                        current_key = key

                        if tableName == 'fares':
                                current_fares = tableAttributes
                        else:
                                current_trips = tableAttributes
			
if current_key == key: 
	allAttributes = []
        allAttributes.extend(current_trips)
        allAttributes.extend(current_fares)
        fare_amount = allAttributes[11]
        fare_amount = float(fare_amount)	

	if fare_amount <= 10.00:
		above10 += 1
	else:
		pass
	
	print above10



