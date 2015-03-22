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
		for item in final_output.items():
#			n += 1
#			print str(n), key, item[0]

		 	s1 = [i for i in eval(item[0])]
			s1.extend(item[1]) 
			s1.extend(tableAttributes) 
			n += 1
			print "%s\t%s" % (key, s1[1:])
 
		final_output = {} 
print n 		 
