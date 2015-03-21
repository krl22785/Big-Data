#!/usr/bin/env python

import sys

import csv

f = open("licenses.csv")
reader = csv.reader(f)

license_storage = {}

for line in reader:
        license_storage[line[0]] = line[1:]

current_key = None
current_fares = []
current_trips = []
n = 0

for line in sys.stdin:
	key, value = line.split('\t')
        value = eval(value)
	
	try:
		key = eval(key) 
		print key 
	except SyntaxError:
		print "ERRROROORR" 
