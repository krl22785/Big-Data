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
				

vehicle_summary = {} 
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
		vehicle = s1[25]
		fare = float(s1[14])
		surcharge = float(s1[15])
		tip = float(s1[17])
		tolls = float(s1[18])
		total = fare + surcharge + tip + tolls  
	
		if total > 0:
			tip_pct = tip / total
		else:
			tip_pct = 0 

		if vehicle not in vehicle_summary:
			vehicle_summary[vehicle] = {}
			vehicle_summary[vehicle]["total"] = total
			vehicle_summary[vehicle]["tip_pct"] = tip_pct
			vehicle_summary[vehicle]["count"] = 1
	
		else:
			vehicle_summary[vehicle]["total"] += total
        		vehicle_summary[vehicle]["tip_pct"] += tip_pct
          	      	vehicle_summary[vehicle]["count"] += 1

for item in vehicle_summary.items():
	print "%s, %s, %s, %.2f" % (item[0], item[1]["count"], item[1]["total"], item[1]["tip_pct"]/item[1]["count"]) 
