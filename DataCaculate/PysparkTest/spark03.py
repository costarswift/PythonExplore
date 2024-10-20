
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:\software\Python311/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_03")

sc = SparkContext(conf=conf)

rdd = sc.parallelize(["Hello World", "Hi python", "hello spark"])
rdd2 = rdd.flatMap(lambda x: x.split(" "))

print(rdd2.collect())