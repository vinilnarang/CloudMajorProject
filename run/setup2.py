import os,sys

def didItWork():
	temp=raw_input('Y/N : ')
	if temp=='Y' or temp=='y':
		return
	elif temp=='N' or temp=='n':
		sys.exit()
	else:
		didItWork()

#STORING THE FILE IN HDFS
didItWork()
print "*****************************DEMANDING FILE NAME**********************************"
fileName = raw_input("Enter File Name : ")
command = "hdfs dfs -put %s /user/hdfs/" % fileName
os.system(command)

#HBASE CREATING TABLE
didItWork()
tableName = fileName.split('.')[0]
tempString = "create '%s', {NAME => 'f'},   {SPLITS => ['g', 'm', 'r', 'w']}" % tableName
tempFile = open("temp", "w")
tempFile.write(tempString)
tempFile.close()
os.system("hbase shell < temp")
os.system("rm temp")

#HBASE MAP AND REDUCE
didItWork()
tempString = "hadoop jar /usr/lib/hbase/hbase-0.94.6-cdh4.4.0-security.jar importtsv -Dimporttsv.separator=, -Dimporttsv.bulk.output=$1 -Dimporttsv.columns=HBASE_ROW_KEY,f:count $1 /user/hdfs/$2"
tempFile = open("mapReduce.sh", "w")
tempFile.write(tempString)
tempFile.close()
command = "./mapReduce.sh %s %s" % (tableName,fileName)
os.system(command)
os.system("rm mapReduce.sh")

#LOAD THE TABLE
didItWork()
command = "hbase org.apache.hadoop.hbase.mapreduce.LoadIncrementalHFiles %s %s" % (tableName,tableName)
os.system(command)
