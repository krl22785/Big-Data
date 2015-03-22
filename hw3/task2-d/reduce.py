#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
dates = {} 

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
	
        		revenue_date = allAttributes[2][0:10]
			fare_amount = float(allAttributes[11]) 
			surcharge_amount = float(allAttributes[12])    		   
			tip_amount = float(allAttributes[14]) 
			tolls_amount = float(allAttributes[15]) 
			
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






