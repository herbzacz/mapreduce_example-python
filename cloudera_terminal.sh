hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \ 
-input /user/cloudera/map_reduce_input \ #Input file
-output /user/cloudera/map_reduce_output \ #Output file
-mapper /home/cloudera/fh_wn/week2/wc_mapper.py \ #run Mapper.py File
-reducer /home/cloudera/fh_wn/week2/wc_reducer.py \ #run Reducer.py File 
-file /home/cloudera/fh_wn/week2/wc_mapper.py \ #Mapper.py Repo
-file /home/cloudera/fh_wn/week2/wc_reducer.py  #Reducer.py Repo

cat *.txt | ./wc_mapper.py | sort | ./wc_reducer.py
