#!/usr/bin/env python

import sys
import csv

current_key = None
top_k = {}

total_fare = 0

for line in sys.stdin:

        key, value = line.split('\t')

	value1 = eval(value)

        tableName = value1[0]

        tempAttributes = value1[1]
        tableAttributes = tempAttributes.split("??")

	#print tableAttributes

	if tableName != 'licenses':

		if key == current_key:

			if tableName == 'fares':
                        	current_fares = float(tableAttributes[0])
				total_fare += current_fares
                	else:
                        	pass

		else:
			current_key = key

			if tableName == 'fares':
                               	current_fares = float(tableAttributes[0])
				total_fare += current_fares
                      	else:
                               	pass

	else:
		atts = value1[1].split("??")
		agent_name = atts[9]

		if agent_name in top_k:
			top_k[agent_name] += total_fare
		else:
			top_k[agent_name] = total_fare

		total_fare = 0

sorted_k = sorted(top_k.items(), key = lambda x: -x[1])

final_output = sorted_k[0:10]

for item in final_output:
	print "%s\t%s" % (item[0], item[1])
