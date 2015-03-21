#!/usr/bin/env python

import sys

import csv 

f = open("licenses.csv") 
reader = csv.reader(f) 

license_storage = {} 

for line in reader: 
	license_storage[line[0]] = line[1:] 

current_key = None
current_fares = []
current_trips = []
n = 0 

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
			
			try:
				temp = eval(key)			
				key_medallion = temp[0]

			except SyntaxError: 
				pass

			if key_medallion in license_storage:
				allAttributes.extend(license_storage[key_medallion]) 
				print "%s\t%s" % (current_key, allAttributes) 
				n += 1
				
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
	if key_medallion in license_storage:
		allAttributes.extend(license_storage[key_medallion])
		print "%s\t%s" % (current_key, allAttributes)
		n += 1

print n

