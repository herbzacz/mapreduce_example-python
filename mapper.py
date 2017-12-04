#!/usr/bin/env python 
import sys 

#For-Loop, which seperates words
for line in sys.stdin: 
  line = line.strip() #removes spaces
  keys = line.split(" ") #splits them
  value = 1

#For-Loop, which seperates words and adds the number 1 to it (key-value-pair)
for item in keys: 
  print( '%s\t%s' % (item, value) )  #Output with tabs