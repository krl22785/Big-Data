#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = [] 
storage = {} 
n = 0 

for line in sys.stdin:

        key, value = line.split('\t')
        value = eval(value)

        tableName = value[0]

        tempAttributes = value[1]
        tableAttributes = tempAttributes.split(",")

	if tableName != 'licenses':  
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

                	#print "%s\t%s" % (current_key, allAttributes)
			
				storage[current_key] = allAttributes 
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
	else:

		for item in storage.items():
			s1 = [i for i in eval(item[0])] 
			s1.extend(item[1]) 
			s1.extend(tableAttributes) 
			n += 1
			print "%s\t%s" % (s1[0], s1[1:])  

		storage = {} 
			
print n 

if current_key == key: 
	allAttributes = []
        allAttributes.extend(current_trips)
        allAttributes.extend(current_fares)
        print "%s\t%s" % (current_key, allAttributes)

