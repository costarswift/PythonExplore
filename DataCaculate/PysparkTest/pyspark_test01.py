
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)

rdd = sc.textFile("D:\code\Python\PythonExplore\DataCaculate\PysparkTest\words.txt")

print(rdd.collect())