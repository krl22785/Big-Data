#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
n = 0 
final_output = {} 

for line in sys.stdin:
	
        key, value = line.split('\t')
        value = eval(value)

        tableName = value[0]

        tempAttributes = value[1]
        tableAttributes = tempAttributes.split(",")

	if tableName != "licenses":

		if key == current_key:
	
                	if tableName == 'fares':
                        	current_fares = tableAttributes
                	else:
                        	current_trips = tableAttributes

			allAttributes = []
                        allAttributes.extend(current_trips)
                        allAttributes.extend(current_fares)

			if len(allAttributes) == 17:
                                final_output[current_key] = allAttributes
                                current_trips = []
                                current_fares = []
			else:
				current_trips = [] 
				current_fares = [] 

        	else: 
			current_key = key 

			if tableName == 'fares':
                               	current_fares = tableAttributes
                      	else:
                               	current_trips = tableAttributes 
		 
	else:	
		for obs in final_output.items():
			
			compare_key = eval(obs[0])[0]

			if compare_key == key:
				s1 = [i for i in eval(obs[0])] 
				s1.extend(obs[1])
				s1.extend(tableAttributes)
				print "%s\t%s" % (s1[0], s1[1:])  
			else:
				pass 

		final_output = {}








 
