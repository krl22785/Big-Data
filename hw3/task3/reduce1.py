#!/usr/bin/env python

import sys

current_key = None
current_fares = []
current_trips = []
license_storage = {}
n = 0

for line in sys.stdin:

	key, value = line.split('\t')
        value = eval(value)

        tableName = value[0]

        tempAttributes = value[1]
        tableAttributes = tempAttributes.split(",")

	if tableName in license_storage:
		license_storage[tableName] += 1
		n += 1
		print n
	else:
		license_storage[tableName] = 1

print n 
print license_storage
