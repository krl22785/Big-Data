#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
driver_medallions = {} 

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
			hack_license = temp[1] 			

			if hack_license not in driver_medallions:
				driver_medallions[hack_license] = [] 
				driver_medallions[hack_license].append(medallion) 
			else:
				driver_medallions[hack_license].append(medallion)			

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
	
	if hack_license not in driver_medallions:
		driver_medallions[hack_license] = []
		driver_medallions[hack_license].append(medallion) 
	else: 
		driver_medallions[hack_license].append(medallion) 


for i in driver_medallions.items():
	print "%s\t%s" % (i[0], len(set(i[1]))) 






 
