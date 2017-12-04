## MapReduce in Python

![MapReduce](http://wi-wiki.de/lib/exe/fetch.php?media=bigdata:mapreducewordcountoverview1.png)
Source: http://wi-wiki.de  

#mapper.py  
```
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
```

#reducer.py
```
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
 ```
Code example:
http://www.science.smith.edu/dftwiki/index.php/Hadoop_Tutorial_2_--_Running_WordCount_in_Python

MapReduce paper:
https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf
