

from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:\software\Python311/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_02")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())