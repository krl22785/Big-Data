#!/usr/bin/python

import sys
import os
import csv

for line in sys.stdin:

	#env = os.chdir['HOME']
	#env = os.environ["mapreduce_map_input_file"]

	line = line.strip()
	splits = line.split(",")

	if len(splits) == 11:

		key1 = splits[0]
		key2 = splits[1]
		key3 = splits[2]
		key4 = splits[3]
		keyAttributes = (key1, key2, key3, key4)

		otherAttributes = splits[10]
		#otherAttributes = "??".join(splits[4:])

		valuePair = ("fares", otherAttributes)

		if key1 != 'medallion':
			print "%s\t%s" % (keyAttributes, valuePair)
		else:
			pass

	elif len(splits) == 14:

		key1 = splits[0]
		key2 = splits[1]
		key3 = splits[2]
		key4 = splits[5]
		keyAttributes = (key1, key2, key3, key4)

		other1 = "??".join(splits[3:5])
		other2 = "??".join(splits[6:])
		otherAttributes = other1 + "," + other2
		valuePair = ("trips", otherAttributes)

		if key1 != 'medallion':
			print "%s\t%s" % (keyAttributes, valuePair)
		else:
			pass

	else:
		newline = line.splitlines()
		reader = csv.reader(newline)
		lic_output = next(reader)

		key1 = lic_output[0]
		keyAttributes = (key1)
		otherAttributes = "??".join(lic_output[1:])

		valuePair = ("licenses", otherAttributes)

		if key1 != 'medallion':
			print "%s\t%s" % (key1, valuePair)
		else:
			pass
