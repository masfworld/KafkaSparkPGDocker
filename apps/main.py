import os
from tkinter.dnd import dnd_start
from pyspark.sql import SparkSession
from pyspark.sql.functions import *



def init_spark():
    print("Creating session")
    spark = SparkSession.builder.appName("EDEM_APP").getOrCreate()
    return spark

def main():
    spark=init_spark()
    stream_detail_df = spark.readStream.format("kafka")\
                    .option("kafka.bootstrap.servers", "kafka0:29092")\
                    .option("subscribe", "mocked_data")\
                    .option("startingOffsets", "earliest")\
                    .load() 
    
    stream_detail_df.printSchema()
    ds = stream_detail_df.selectExpr("CAST(value AS STRING)")
    print(type(stream_detail_df))
    print(type(ds))
    rawQuery = ds.writeStream.queryName("qraw").format("memory").start()
    raw = spark.sql("select * from qraw")
    print("#####################")
    raw.show()
    print("#####################")
    dataQuery = ds.writeStream.queryName("qdata").format("memory").start()
    alerts = spark.sql("select * from qdata")
    print("#####################")
    alerts.show()
    print("#####################")
    #data = spark.sql("select * from qdata")
    #data.show()


if __name__ == '__main__':
  main()