#!/usr/bin/env python

import sys

date_sum = {} 

for line in sys.stdin:

        key, value = line.split('\t')
        value = eval(value)
	
	fare = float(value[0])
	surcharge = float(value[1])
	tips = float(value[2])
	tolls = float(value[3])
	
	if key in date_sum:
		date_sum[key]["fare"] += fare
		date_sum[key]["surcharge"] += surcharge
		date_sum[key]["tips"] += tips
		date_sum[key]["tolls"] += tolls
	else:
		date_sum[key] = {} 
		date_sum[key]["fare"] = fare
                date_sum[key]["surcharge"] = surcharge
                date_sum[key]["tips"] = tips
                date_sum[key]["tolls"] = tolls

for item in date_sum.items():
#	print item[0], item["fare"], item["surcharge"], item["tips"], item["tolls"]

	print "%s\t(%.2f, %.2f, %.2f, %.2f)" % (item[0], item[1]["fare"], item[1]["surcharge"], item[1]["tips"], item[1]["tolls"]) 
