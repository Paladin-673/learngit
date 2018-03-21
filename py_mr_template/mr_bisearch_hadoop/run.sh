
HADOOP_CMD="/usr/local/src/hadoop-1.2.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"

INPUT_FILE_PATH_1="/query_cookie_ip.txt"
OUTPUT_PATH="/output_ip_lib"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_SORT_PATH

#Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func IPLIB" \
    -reducer "cat" \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf "mapreduce.reduce.memory.mb=5000" \ #fields 2 to sort
    -jobconf "mapred.job.name=ip_lib_demo" \     #fields 1 to bucket and sort
    -cacheFile "hdfs://master:9000/ip.lib.txt#IPLIB" \
    -file "./map.py"
