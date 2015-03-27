#!/usr/bin/env python

import sys

med_trips = {} 

for line in sys.stdin:

        key, value = line.split('\t')
        medallion = key
	count = int(value) 

	if medallion in med_trips:
		med_trips[medallion] += count 
	else:
		med_trips[medallion] = count

for item in med_trips.items():
	print "%s\t%s" % (item[0], item[1]) 


