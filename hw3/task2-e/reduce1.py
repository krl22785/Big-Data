#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
medallion_trips = {} 

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

        		temp = eval(key) 
			medallion = temp[0]

			if medallion not in medallion_trips: 
				medallion_trips[medallion] = 1
			else:
				medallion_trips[medallion] += 1         
	
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

	if medallion not in medallion_trips:
        	medallion_trips[medallion] = 1
	else:
		medallion_trips[medallion] += 1

finalOutput = sorted(medallion_trips.items(), key = lambda x: -x[1])

for med in finalOutput:
        print "%s\t%s" % (med[0], med[1])




