set -e -x

HADOOP_CMD="/usr/local/src/hadoop-1.2.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"

INPUT_FILE_PATH_A="/a.txt"
INPUT_FILE_PATH_B="/b.txt"

OUTPUT_SORT_PATH="/output_sort"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_SORT_PATH

#Step 3.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_A,$INPUT_FILE_PATH_B \
    -output $OUTPUT_SORT_PATH \
    -mapper "python map_sort.py" \
    -reducer "python reduce_sort.py" \
    -file ./map_sort.py \
    -file ./reduce_sort.py \
    -jobconf mapred.reduce.tasks=2 \
    -jobconf stream.num.map.output.key.fields=2 \ #fields 2 to sort
    -jobconf num.key.fields.for.partition=1 \     #fields 1 to bucket and sort
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
