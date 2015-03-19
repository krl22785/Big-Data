#!/usr/bin/env python

import sys

current_key = None 
current_fares = [0]
current_trips = [0] 
finalAttributes = []

dates = {} 

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
		
		
		revenue_date = allAttributes[9][0:10]
		fare_amount = float(allAttributes[1])
		surcharge_amount = float(allAttributes[2])
		tip_amount = float(allAttributes[4])
		tolls_amount = float(allAttributes[5])
 		 		
		#print revenue_date, fare_amount, surcharge_amount, tip_amount, tolls_amount
		if revenue_date not in dates: 
			dates[revenue_date] = {} 
			dates[revenue_date]["fare"] = fare_amount 
			dates[revenue_date]["surcharge"] = surcharge_amount 
			dates[revenue_date]["tip"] = tip_amount
			dates[revenue_date]["tolls"] = tolls_amount 

		else: 		
			dates[revenue_date]["fare"] += fare_amount 
			dates[revenue_date]["surcharge"] += surcharge_amount
			dates[revenue_date]["tip"] += tip_amount
			dates[revenue_date]["tolls"] += tolls_amount		
	
finalOutput = sorted(dates.items(), key = lambda x: x[0]) 

for rev in finalOutput:	
	print "%s\t(%.2f, %.2f, %.2f, %.2f)" % (rev[0], rev[1]["fare"], rev[1]["surcharge"], rev[1]["tip"], rev[1]["tolls"]) 




 


#if current_key == key:
#	allAttributes =  []
 #       allAttributes.extend(current_fares)
  #      allAttributes.extend(current_trips)
