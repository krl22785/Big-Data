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
				

top_k = {} 
test = {} 

for item in storage.items():
	compare_value = eval(item[0])[0]
	s1 = [i for i in eval(item[0])] 
	s1.extend(item[1])

	try: 
		s1.extend(license_storage[compare_value])
	except:
		pass
	
	if len(s1) != 35:
		pass
	else:
		agent_name = s1[29]
		fare = float(s1[14])
		surcharge = float(s1[15])
		tip = float(s1[17])
		tolls = float(s1[18])
		total = fare + surcharge + tip + tolls  
		
		if agent_name in top_k:
			top_k[agent_name] += total 
		else:
			top_k[agent_name] = total 

final_output = sorted(top_k.items(), key = lambda x: - x[1])
limit = 0 
for item in final_output:
	if limit < 10:
		print "%s\t%s" % (item[0], item[1]) 
		limit += 1
	else:
		break
