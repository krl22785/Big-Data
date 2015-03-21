#!/usr/bin/env python

import sys

for line in sys.stdin:
	key, value = line.split('\t')

	print [i for i in eval(key)] 	
	
