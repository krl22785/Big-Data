#!/usr/bin/env python

import sys

fare_dist = {} 

for line in sys.stdin:

        key, value = line.split('\t')
       	fare = float(key) 
	count = int(value) 

	if fare in fare_dist:
		fare_dist[fare] += 1
	else:
		fare_dist[fare] = 1 

final_output = sorted(fare_dist.items(), key = lambda x: -x[1]) 

for item in final_output:
	print "%s\t%s" % (item[0], item[1])  
