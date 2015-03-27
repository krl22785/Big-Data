#!/usr/bin/env python

import sys

pass_dist = {} 

for line in sys.stdin:

        key, value = line.split('\t')
        passenger_cnt = int(key)
	count = int(value) 

	if passenger_cnt in pass_dist:
		pass_dist[passenger_cnt] += 1
	else:	
		pass_dist[passenger_cnt] = 1

final_output = sorted(pass_dist.items(), key = lambda x: -x[1]) 

for item in final_output:
	print "%s\t%s" % (item[0], item[1]) 
