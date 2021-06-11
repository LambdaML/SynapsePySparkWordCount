import sys
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":
	
	# create Spark context with necessary configuration
	conf = SparkConf().setAppName("WordCount").set("spark.hadoop.validateOutputSpecs", "false")
	sc = SparkContext(conf=conf)
	
	# read data from text file and split each line into words
	words = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))
	
	# count the occurrence of each word
	counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
	
	# save the counts to output
	counts.saveAsTextFile(sys.argv[2])
