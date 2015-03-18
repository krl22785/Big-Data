#!/usr/bin/python

import sys
import os


for line in sys.stdin:
	
	#env = os.chdir['HOME']
	#env = os.environ["mapreduce_map_input_file"]	
 	
	line = line.strip() 
	splits = line.split(",")

	if len(splits) == 11: 
		
		keyAttributes = splits[0:4]
		otherAttributes = splits[4:] 
		valuePair = ("fares", otherAttributes) 
		
		print "%s\t%s" % (keyAttributes, valuePair) 
		
	else:
		
		keyAttributes = [] 
		keyAttributes.append(splits[0])
                keyAttributes.append(splits[1])
                keyAttributes.append(splits[2])
		keyAttributes.append(splits[5])
			
		otherAttributes = []
		rate_code, store_and_fwd_flag = splits[3:5]
		otherAttributes.append(rate_code)
		otherAttributes.append(store_and_fwd_flag)
		otherAttributes.extend(splits[6:])
		valuePair = ("trips", otherAttributes) 	
	
		print "%s\t%s" % (keyAttributes, valuePair)
