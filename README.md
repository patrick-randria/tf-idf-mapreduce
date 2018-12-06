# TF-IDF with Mapreduce & Python

Compute [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) using Python with Hadoop Streaming.

## Term Frequency — Inverse Document Frequency
It stands to statistically measure how important a word is in a collection of documents.

We will use the formula
```
w_t,d = (tf_t,d / n_d) x log(N/df_t)
```

## Prepare data
We will first copy input data to HDFS.
```
$ hadoop fs -mkdir input
$ hadoop fs -copyFromLocal input /input
```

## Step 1 - Wordcount
Execute first step with Hadoop streaming

```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
   -input /your_hdfs_path/input/* \
	-output /your_hdfs_path/results/step_1 \
	-mapper 1_wordcount_mapper.py \
	-reducer 1_wordcount_reducer.py
```
