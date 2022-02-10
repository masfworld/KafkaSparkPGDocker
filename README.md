Steps to run:

1) docker-compose build
2) docker-compose up
3) Navigate to localhost:8080 and check topic mock_data exist if not create
4) Execute the following command:
   
docker exec mda_dp1-spark-master-1 /opt/spark/bin/spark-submit --master spark://spark-master:7077  --jars /opt/spark-apps/postgresql-42.2.22.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.2  --driver-memory 1G --executor-memory 1G /opt/spark-apps/main.py