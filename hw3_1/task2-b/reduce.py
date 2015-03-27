#!/usr/bin/env python

import sys

total_dist = {} 

for line in sys.stdin:

        key, value = line.split('\t')
       	total = float(key)
	count = int(value)

	if total in total_dist:
		total_dist[total] += 1
	else: 
		total_dist[total] = 1

print sum(total_dist.values()) 
