#!/usr/bin/env python

import sys
import csv

current_key = None
top_med = {}
top_k = {} 

total_fare = 0

for line in sys.stdin:

        key, value = line.split('\t')
	value1 = eval(value)
        tableName = value1[0]
        tempAttributes = value1[1]
        tableAttributes = tempAttributes.split("??")

	if tableName != 'licenses':
		key1 = eval(key)	
		medallion = key1[0]	

		if tableName == 'fares':

			if medallion in top_med:
				top_med[medallion] += float(tableAttributes[0])
			else:
				top_med[medallion] = float(tableAttributes[0])
		else:
			pass
	else:
		#print key 
#new = sorted(top_med.items(), key = lambda x: -x[1])[0:20]
#for item in new:
#	print item[0], item[1]
 
		atts = value1[1].split("??") 			
		agent_name = atts[9] 
		medallion = key	
 			
		try:
			medallion_revenue = top_med[medallion]
		except:
			medallion_revenue = 0 		
		
		if agent_name in top_k:
			top_k[agent_name] += medallion_revenue 
		else:
			top_k[agent_name] =  medallion_revenue 

sorted_k = sorted(top_k.items(), key = lambda x: -x[1]) 

final_output = sorted_k[0:10]

for item in final_output:
	print "%s\t%s" % (item[0], item[1])			
