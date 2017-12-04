#!/usr/bin/env python
import sys

#initalizing variables
last_key = None
running_total = 0

#For-Loop
for line in sys.stdin:
    this_key, value = line.split('\t') #seperates values
    value = int(value) #changes to integers
    if this_key == last_key:
        running_total += value #adds up values
    else:
    if last_key:
        print( '%s\t%s' % (last_key, running_total) )
        last_key = this_key
        running_total = value
        print( '%s\t%s' % (last_key, running_total) ) #Output 
