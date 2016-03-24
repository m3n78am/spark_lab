#!/usr/bin/python

import os
import sys
from pyspark import SparkConf,SparkContext

sys.path.append(os.path.dirname(__file__) + "/lib")
sys.path.append(os.path.dirname(__file__))


os.system("hadoop fs -rmr /user/humingqiang/spark_lab/trainning_data/result")

class trainedData():
	def __init__(self,class2,class3,name3,kdtId,goodsId,title):
		self.class2 = class2
		self.class3 = class3
		self.name3 = name3
		self.kdtId = kdtId
		self.goodsId = goodsId
		self.title = title

sc = SparkContext()
sc.addPyFile(os.path.dirname(__file__) + "/lib/jieba.zip")
sc.addPyFile(os.path.dirname(__file__) + "/lib/util.py")


from util import parse
import jieba



# application
rawdata = sc.textFile("/user/humingqiang/spark_lab/trainning_data/trained_data.dat").filter(lambda line:parse(line) is not None)


wordRDD = rawdata.flatMap(lambda x: jieba.cut(x))
wordFreRDD = wordRDD.map(lambda x: (x.encode("utf8"), 1))
counts = wordFreRDD.reduceByKey(lambda a,b: a + b)

#tds = headdata.map(lambda line: jiebav2.posseg.cut(line.strip("\n").split(",")[-1]))
counts.saveAsTextFile("/user/humingqiang/spark_lab/trainning_data/result")

sc.stop()
