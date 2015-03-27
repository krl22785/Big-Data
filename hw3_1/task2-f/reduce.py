#!/usr/bin/env python

import sys

hack_dict = {} 

for line in sys.stdin:

        key, value = line.split('\t')
        
	if key not in hack_dict:
		hack_dict[key] = []
		hack_dict[key].append(value) 
	else:
		hack_dict[key].append(value) 

for item in hack_dict.items():
	print "%s\t%s" % (item[0], len(set(item[1])))

 
