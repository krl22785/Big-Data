#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
passenger_distribution = {} 



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
		
			passenger_amount = allAttributes[3]		                	
 			
			if passenger_amount in passenger_distribution:
                        	passenger_distribution[passenger_amount] += 1
                	else:
                        	passenger_distribution[passenger_amount] = 1

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
        
	passenger_amount = allAttributes[3]

        if passenger_amount in passenger_distribution:
        	passenger_distribution[passenger_amount] += 1
        else:
                passenger_distribution[passenger_amount] = 1

finalOutput = sorted(passenger_distribution.items(), key = lambda x: -x[1])

for pas in finalOutput:
        print "%s\t%s" % (pas[0], pas[1])











