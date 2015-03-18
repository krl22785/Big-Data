#!/usr/bin/python

import sys

for line in sys.stdin:

	line = line.strip() 
	splits = line.split(",")

	if len(splits) == 11: 
		
		medallion = splits[0]
		hack_license = splits[1]
		vendor_id = splits[2]
		pickup_datetime = splits[3]
		id = (medallion, hack_license, vendor_id, pickup_datetime)
		 
		vals = ",".join(splits[4:]) 
		print "(%s,%s,%s,%s)\t(%s)" % (id[0], id[1], id[2], id[3], vals)  		
	
	else:

		medallion = splits[0]
                hack_license = splits[1]
                vendor_id = splits[2]
		pickup_datetime = splits[5]
		
		rate_code, store_and_fwd_flag = splits[3:5]

		dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude = splits[6:]

		id = (medallion, hack_license, vendor_id, pickup_datetime)
		
		print "(%s,%s,%s,%s)\t(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (id[0], id[1], id[2], id[3], rate_code, store_and_fwd_flag, \
							dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, \
							pickup_latitude, dropoff_longitude, dropoff_latitude)
