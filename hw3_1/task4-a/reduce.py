#!/usr/bin/env python

import sys
import csv

veh_type = {} 

for line in sys.stdin:

        key, value = line.split('\t')

	type = key 

	info = eval(value) 
	cnt = int(info[0])
	total = float(info[1])

	tip = float(info[2]) 

	if total == 0:
		tip_pct = 0 
	else:
		tip_pct =  tip/total 

	if type not in veh_type:
		veh_type[type] = {} 
		veh_type[type]["trips"] = cnt 
		veh_type[type]["total"] = total
		veh_type[type]["tip_pct"] = tip

	else:
		veh_type[type]["trips"] += cnt
                veh_type[type]["total"] += total
                veh_type[type]["tip_pct"] += tip 

for item in veh_type.items():
	print "%s\t(%s, %.2f, %.2f)" % (item[0], item[1]["trips"], item[1]["total"], item[1]["tip_pct"]/item[1]["trips"]) 
	
