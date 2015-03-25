#!/usr/bin/env python

import sys
import csv 

current_key = None
current_fares = []
current_trips = [] 
storage = {}  
license_storage = {} 

n = 0

for line in sys.stdin:

        key, value = line.split('\t')
        
	value1 = eval(value)

        tableName = value1[0]
	#print tableName
        tempAttributes = value1[1]
        tableAttributes = tempAttributes.split("??")
	
	
	if tableName != 'licenses': 
 	 	
		if key == current_key:

			if tableName == 'fares':
                        	current_fares = tableAttributes
                	else:
                        	current_trips = tableAttributes	
	

			allAttributes = []
                        allAttributes.extend(current_trips)
                        allAttributes.extend(current_fares)
  
			storage[current_key] = allAttributes 
 
			current_trips = [] 
			current_fares = []			
		else: 
			current_key = key 

			if tableName == 'fares':
                               	current_fares = tableAttributes
                      	else:
                               	current_trips = tableAttributes 
	else:
		license_storage[key] = value1[1].split("??")
				

for item in storage.items():
	compare_value = eval(item[0])[0]
	s1 = [i for i in eval(item[0])] 
	s1.extend(item[1])
	
	try:
		toAdd = license_storage[compare_value]
		s1.extend(license_storage[compare_value])
		if len(s1) != 35:
			pass
		else:		
			print "%s\t%s" % (s1[0], s1[1:]) 
			n += 1
	except:
		pass 

print n 
